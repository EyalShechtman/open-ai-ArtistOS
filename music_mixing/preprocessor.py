import json
import librosa
import pandas as pd
from api import QwenAPI
import numpy as np

class PreProcessor:
    def __init__(self):
        self.songs = []
        self.qwen = QwenAPI()
        self.df_data = []
    
    def get_songs(self):
        import os
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        songs_path = os.path.join(script_dir, "data", "songs.json")
        with open(songs_path, "r") as f:
            self.songs = json.load(f)
        return self.songs
    
    def _stats(self, x, name):
        x = np.asarray(x, float)
        return {
            f"{name}_mean": float(np.mean(x)),
            f"{name}_std":  float(np.std(x)),
            f"{name}_min":  float(np.min(x)),
            f"{name}_max":  float(np.max(x)),
        }

    def extract_features(self, mp3_path, sr_target=22050):
        # stable I/O
        y, sr = librosa.load(mp3_path, sr=sr_target, mono=True)
        y, _ = librosa.effects.trim(y, top_db=30)
        dur = librosa.get_duration(y=y, sr=sr)
        if dur < 6:  # guard for very short clips
            pad = int((6 - dur) * sr)
            y = np.pad(y, (0, pad))
            dur = librosa.get_duration(y=y, sr=sr)

        # slices
        n5 = int(5 * sr)
        first, last = y[:n5], y[-n5:]

        # global tempo + beats (more stable than per-slice tempo alone)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        f_tempo, _ = librosa.beat.beat_track(y=first, sr=sr)
        l_tempo, _ = librosa.beat.beat_track(y=last,  sr=sr)

        # timbre & harmony
        S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512, center=True)) + 1e-9
        mfcc = librosa.feature.mfcc(S=librosa.power_to_db(S**2), sr=sr, n_mfcc=13)
        chroma = librosa.feature.chroma_stft(S=S, sr=sr)

        sc = librosa.feature.spectral_centroid(S=S, sr=sr)
        sro = librosa.feature.spectral_rolloff(S=S, sr=sr, roll_percent=0.85)
        zcr = librosa.feature.zero_crossing_rate(y, frame_length=2048, hop_length=512)

        # slices (same features for first/last)
        def slice_feats(sig):
            S_ = np.abs(librosa.stft(sig, n_fft=2048, hop_length=512, center=True)) + 1e-9
            return {
                **self._stats(librosa.feature.chroma_stft(S=S_, sr=sr).mean(axis=1), "slice_chroma"),
                **self._stats(librosa.feature.mfcc(S=librosa.power_to_db(S_**2), sr=sr, n_mfcc=13).mean(axis=1), "slice_mfcc"),
                "slice_centroid_mean": float(librosa.feature.spectral_centroid(S=S_, sr=sr).mean()),
            }

        feats = {
            "duration_sec": float(dur),
            "tempo_bpm": float(tempo),
            "tempo_first5_bpm": float(f_tempo),
            "tempo_last5_bpm": float(l_tempo),
            "n_beats": int(len(beats)),

            "centroid_mean": float(sc.mean()),
            "centroid_std":  float(sc.std()),
            "rolloff_mean":  float(sro.mean()),
            "zcr_mean":      float(zcr.mean()),
            **self._stats(mfcc.mean(axis=1), "mfcc"),
            **self._stats(chroma.mean(axis=1), "chroma"),

            **{f"first_{k}": v for k,v in slice_feats(first).items()},
            **{f"last_{k}":  v for k,v in slice_feats(last).items()},
        }
        return feats
    
    def process_songs(self):
        songs = self.get_songs()
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        for song in songs:
            mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
            print(f"Processing: {song['name']} by {song['artist']}")
            
            # Upload and get Qwen analysis
            url = self.qwen.upload_temp_mp3(mp3_path)
            qwen_result, _ = self.qwen.call_qwen(url)
            
            # Extract audio features
            features = self.extract_features(mp3_path)
            
            # Combine all data
            row = {
                'id': song['id'],
                'name': song['name'],
                'artist': song['artist'],
                'qwen_analysis': qwen_result,
                **features
            }
            self.df_data.append(row)
            print(f"Completed: {song['name']}")
    
    def save_to_csv(self, filename="processed_songs.csv"):
        df = pd.DataFrame(self.df_data)
        df.to_csv(filename, index=False)
        print(f"Saved {len(df)} songs to {filename}")

if __name__ == "__main__":
    processor = PreProcessor()
    processor.process_songs()
    processor.save_to_csv()