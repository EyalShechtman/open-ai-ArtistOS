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
        y, sr = librosa.load(mp3_path, sr=sr_target, mono=True)
        y, _ = librosa.effects.trim(y, top_db=30)
        dur = librosa.get_duration(y=y, sr=sr)
        if dur < 6:
            y = np.pad(y, (0, int((6 - dur) * sr))); dur = librosa.get_duration(y=y, sr=sr)

        # beat/tempo (global)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

        # STFT features (global)
        S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512, center=True)) + 1e-9
        sc = librosa.feature.spectral_centroid(S=S, sr=sr).mean()
        sro = librosa.feature.spectral_rolloff(S=S, sr=sr, roll_percent=0.85).mean()
        zcr = librosa.feature.zero_crossing_rate(y, frame_length=2048, hop_length=512).mean()

        # MFCC (global) – mean/std only
        mfcc = librosa.feature.mfcc(S=librosa.power_to_db(S**2), sr=sr, n_mfcc=13)
        mfcc_mean = float(mfcc.mean())
        mfcc_std  = float(mfcc.std())

        # First/last 5s slices for harmonic + entry/exit energy
        n5 = int(5 * sr)
        first, last = y[:n5], y[-n5:]

        def chroma12(sig):
            S_ = np.abs(librosa.stft(sig, n_fft=2048, hop_length=512, center=True)) + 1e-9
            chroma = librosa.feature.chroma_stft(S=S_, sr=sr)
            # Ensure we get exactly 12 dimensions by taking mean across time
            v = np.mean(chroma, axis=1)
            # Verify it's 12-dimensional
            # assert len(v) == 12, f"Expected 12 chroma dimensions, got {len(v)}"
            v = v / (np.linalg.norm(v) + 1e-9)  # L2 norm for cosine later
            return v.astype(float).tolist()

        def slice_centroid(sig):
            S_ = np.abs(librosa.stft(sig, n_fft=2048, hop_length=512, center=True)) + 1e-9
            return float(librosa.feature.spectral_centroid(S=S_, sr=sr).mean())

        # Extract chroma vectors with validation
        first_chroma = chroma12(first)
        last_chroma = chroma12(last)
        
        # Validate chroma vector dimensions
        # assert len(first_chroma) == 12, f"First chroma vector has {len(first_chroma)} dimensions, expected 12"
        # assert len(last_chroma) == 12, f"Last chroma vector has {len(last_chroma)} dimensions, expected 12"
        
        feats = {
            "duration_sec": float(dur),
            "tempo_bpm": float(tempo),
            "n_beats": int(len(beats)),

            "centroid_mean": float(sc),
            "rolloff_mean": float(sro),
            "zcr_mean": float(zcr),

            "mfcc_mean": mfcc_mean,
            "mfcc_std": mfcc_std,

            # critical for mixing
            "first_chroma_vec_12": first_chroma,
            "last_chroma_vec_12": last_chroma,
            "first_slice_centroid_mean": slice_centroid(first),
            "last_slice_centroid_mean":  slice_centroid(last),
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