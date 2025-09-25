#!/usr/bin/env python3
"""
Simple test script for MixAlgo with 2 random starting songs
"""

import pandas as pd
import random
from mix_algo import MixAlgo

def test_mix_algo():
    # Load data
    df = pd.read_csv("processed_songs.csv")
    print(f"Loaded {len(df)} songs")
    
    # Initialize algorithm
    algo = MixAlgo()
    algo.fit(df)
    
    # Pick 2 random starting songs
    song_ids = list(df['id'].astype(str))
    start_songs = random.sample(song_ids, 2)
    
    print(f"\nTesting with random starting songs: {start_songs}")
    
    # Test each starting song
    for i, start_song in enumerate(start_songs, 1):
        print(f"\n--- Test {i}: Starting with Song {start_song} ---")
        
        # Get song info
        song_info = algo.by_id[start_song]
        print(f"Song: {song_info['name']} by {song_info['artist']} ({song_info['tempo_bpm']:.1f} BPM)")
        
        # Generate 5-song playlist
        playlist = algo.generate_playlist(start_song, length=5)
        
        print("Generated playlist:")
        for song in playlist:
            print(f"  {song['position']}. {song['name']} by {song['artist']} ({song['tempo_bpm']:.1f} BPM)")
        
        # Check for duplicates
        song_ids_played = [song['song_id'] for song in playlist]
        unique_count = len(set(song_ids_played))
        print(f"Unique songs: {unique_count}/5")
        
        # Reset for next test
        algo.reset_history()
    
    print(f"\n✅ Test completed successfully!")

if __name__ == "__main__":
    test_mix_algo()
