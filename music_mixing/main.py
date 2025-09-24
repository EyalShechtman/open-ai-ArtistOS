import os
import json
import pandas as pd
from preprocessor import PreProcessor
from api import Data_Fetcher

def main():
    # Load songs
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "data", "songs.json"), "r") as f:
        songs = json.load(f)[:10]  # First 10 songs
    
    # Download songs first
    print("Downloading songs...")
    data_fetcher = Data_Fetcher()
    for song in songs:
        print(f"Downloading: {song['name']} by {song['artist']}")
        data_fetcher.youtube_search_to_mp3(song["name"], song["artist"], song["id"])
        data_fetcher.cut_song(f'data/{song["id"]}.mp3', 0, 40, f'data/{song["id"]}.mp3')
    
    # Process songs
    processor = PreProcessor()
    for song in songs:
        mp3_path = os.path.join(script_dir, "data", f"{song['id']}.mp3")
        print(f"Processing: {song['name']}")
        
        # Extract features
        features = processor.extract_features(mp3_path)
        
        # Upload and get Qwen analysis
        url = processor.qwen.upload_temp_mp3(mp3_path)
        qwen_result, _ = processor.qwen.call_qwen(url)
        
        # Combine data
        row = {
            'id': song['id'],
            'name': song['name'],
            'artist': song['artist'],
            'qwen_analysis': qwen_result,
            **features
        }
        processor.df_data.append(row)
    
    # Save results
    df = pd.DataFrame(processor.df_data)
    df.to_csv("processed_songs.csv", index=False)
    print(f"Saved {len(df)} songs to processed_songs.csv")

if __name__ == "__main__":
    main()
