#!/usr/bin/env python3
"""
Script to update the processed_songs.csv format to match MixAlgo expectations.
- Preserves existing qwen_analysis data
- Re-extracts only audio features using the new format
- Does NOT re-run Qwen API calls
"""

import pandas as pd
import numpy as np
import librosa
import os
import json
from preprocessor import PreProcessor

def update_csv_format():
    """Update CSV to match MixAlgo expected format"""
    
    # Load existing CSV
    print("Loading existing processed_songs.csv...")
    df_old = pd.read_csv("processed_songs.csv")
    print(f"Found {len(df_old)} songs in existing CSV")
    
    # Load songs metadata
    with open("data/songs.json", "r") as f:
        songs_metadata = json.load(f)
    
    # Create metadata lookup
    songs_by_id = {song['id']: song for song in songs_metadata}
    
    # Initialize preprocessor for feature extraction
    processor = PreProcessor()
    
    # Prepare new data
    new_data = []
    
    for idx, row in df_old.iterrows():
        song_id = int(row['id'])
        print(f"Processing song {song_id}: {row['name']} by {row['artist']}")
        
        # Preserve existing data
        preserved_data = {
            'id': song_id,
            'name': row['name'],
            'artist': row['artist'],
            'qwen_analysis': row['qwen_analysis']  # Keep existing Qwen analysis
        }
        
        # Re-extract audio features using new format
        mp3_path = os.path.join("data", f"{song_id}.mp3")
        
        if os.path.exists(mp3_path):
            try:
                # Extract features using the new method
                features = processor.extract_features(mp3_path)
                
                # Combine preserved data with new features
                new_row = {**preserved_data, **features}
                new_data.append(new_row)
                print(f"  ✓ Successfully updated features for {row['name']}")
                
            except Exception as e:
                print(f"  ✗ Error processing {row['name']}: {e}")
                # Keep old data if feature extraction fails
                new_data.append(preserved_data)
        else:
            print(f"  ✗ MP3 file not found: {mp3_path}")
            # Keep old data if file doesn't exist
            new_data.append(preserved_data)
    
    # Create new DataFrame
    df_new = pd.DataFrame(new_data)
    
    # Save updated CSV
    output_file = "processed_songs_updated.csv"
    df_new.to_csv(output_file, index=False)
    print(f"\nSaved updated data to {output_file}")
    print(f"Total songs processed: {len(df_new)}")
    
    # Show sample of new format
    print("\nSample of new format:")
    print("Columns:", list(df_new.columns))
    print("\nFirst row sample:")
    for col in ['id', 'name', 'artist', 'tempo_bpm', 'first_chroma_vec_12', 'last_chroma_vec_12']:
        if col in df_new.columns:
            value = df_new.iloc[0][col]
            if col in ['first_chroma_vec_12', 'last_chroma_vec_12']:
                print(f"  {col}: {type(value)} with {len(value) if isinstance(value, list) else 'N/A'} elements")
            else:
                print(f"  {col}: {value}")
    
    return df_new

if __name__ == "__main__":
    df_updated = update_csv_format()
