import os
import json
import pandas as pd
from preprocessor import PreProcessor
from api import Data_Fetcher

def main():
    # Load songs
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Go up one level to reach data/
    with open(os.path.join(script_dir, "data", "songs.json"), "r") as f:
        songs = json.load(f)[-7:-1]  # Last 7 songs
    
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
    
    # Save results - append to existing CSV or create new one
    df = pd.DataFrame(processor.df_data)

    # Get path to processed_songs.csv in parent directory
    csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "processed_songs.csv")

    # Check if CSV already exists and append to it
    if os.path.exists(csv_path):
        existing_df = pd.read_csv(csv_path)
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        combined_df.to_csv(csv_path, index=False)
        print(f"Added {len(df)} new songs to processed_songs.csv (total: {len(combined_df)} songs)")
    else:
        df.to_csv(csv_path, index=False)
        print(f"Created processed_songs.csv with {len(df)} songs")

if __name__ == "__main__":
    main()
