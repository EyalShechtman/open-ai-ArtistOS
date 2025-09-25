import sys
import os
import time
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from DJ.preprocessor import PreProcessor

def test_feature_extract():
    print(f'{time.time()} start')
    preprocessor = PreProcessor()
    songs = preprocessor.get_songs()
    import os
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mp3_path = os.path.join(script_dir, "data", f"{songs[0]['id']}.mp3")
    features = preprocessor.extract_features(mp3_path)
    print("Features extracted:", list(features.keys()))
    print("First 5s BPM:", features['tempo_first5_bpm'])
    print("Last 5s BPM:", features['tempo_last5_bpm'])
    print("First slice chroma mean:", features['first_slice_chroma_mean'])
    print("Last slice chroma mean:", features['last_slice_chroma_mean'])
    print(f'{time.time()} end')
    return features

if __name__ == "__main__":
    df_data = test_feature_extract()
    df_data = pd.DataFrame([df_data])
    df_data.to_csv('features_test.csv')
    print(df_data)