"""
DJ Music Player - Simple CLI Interface
Uses MixAlgo to create seamless music mixing
"""

import pandas as pd
import random
import subprocess
import threading
import time
from datetime import datetime
from mix_algo import MixAlgo

def log(message):
    """Log with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

class DJPlayer:
    def __init__(self):
        self.algo = MixAlgo()
        self.current_song = 0
        self.playlist = []
        self.is_playing = False
        self.current_process = None
        self.next_process = None
        
    def load_music(self):
        """Load music data and initialize algorithm"""
        print("🎵 Loading music library...")
        df = pd.read_csv("processed_songs.csv")
        self.algo.fit(df)
        print(f"✅ Loaded {len(df)} songs")
        
    def start_mix(self, playlist_length=10):
        """Start a new mix session"""
        log(f"start_mix() called with length={playlist_length}")
        available_songs = list(self.algo.by_id.keys())
        start_song_id = random.choice(available_songs)
        log(f"Selected starting song: {start_song_id}")
        
        print(f"\n🎧 Starting mix session...")
        self.playlist = self.algo.generate_playlist(start_song_id, playlist_length)
        self.current_song = 0
        self.is_playing = True
        log(f"Generated playlist with {len(self.playlist)} songs, current_song={self.current_song}, is_playing={self.is_playing}")
        
        print(f"Generated {len(self.playlist)} song playlist")
        self.show_playlist()
        
    def show_playlist(self):
        """Display current playlist"""
        print(f"\n📋 Current Playlist:")
        for i, song in enumerate(self.playlist):
            marker = "▶️" if i == self.current_song else "  "
            print(f"{marker} {i+1}. {song['name']} by {song['artist']} ({song['tempo_bpm']:.1f} BPM)")
    
    def play_next(self):
        """Play next song in playlist"""
        log(f"play_next() called - current_song={self.current_song}, playlist_length={len(self.playlist)}, is_playing={self.is_playing}")
        
        if not self.is_playing or self.current_song >= len(self.playlist):
            log("Playlist complete or not playing - stopping")
            print("🎉 Playlist complete!")
            self.is_playing = False
            return
            
        song = self.playlist[self.current_song]
        log(f"Playing song {self.current_song + 1}: {song['name']}")
        print(f"\n🎵 Now Playing: {song['name']} by {song['artist']}")
        
        # Stop current audio
        if self.current_process:
            log("Terminating previous audio process")
            self.current_process.terminate()
        
        # Play new song
        audio_path = f"data/{song['song_id']}.mp3"
        log(f"Starting audio process for: {audio_path}")
        print(f"   🎵 Playing: {audio_path}")
        
        # Use sox for better volume control, fallback to afplay
        try:
            # Use sox for volume control capability
            sox_cmd = ['sox', audio_path, '-t', 'coreaudio', 'default', '-q']  # -q for quiet
            self.current_process = subprocess.Popen(sox_cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            log(f"Sox audio process started with PID: {self.current_process.pid}")
        except FileNotFoundError:
            # Fallback to afplay if sox not available
            self.current_process = subprocess.Popen(['afplay', audio_path])
            log(f"Afplay audio process started with PID: {self.current_process.pid}")
        
        # Start monitoring for when song ends
        log("Starting monitor thread")
        monitor_thread = threading.Thread(target=self.monitor_song, daemon=True)
        monitor_thread.start()
        log(f"Monitor thread started: {monitor_thread.name}")
        
        self.current_song += 1
        log(f"Incremented current_song to: {self.current_song}")
    
    def monitor_song(self):
        """Monitor current song and handle crossfade transition"""
        log(f"monitor_song() started - PID: {self.current_process.pid if self.current_process else 'None'}")
        
        if not self.current_process:
            log("No current process to monitor")
            return
        
        # Get the expected song duration and crossfade info
        if self.current_song > 0 and self.current_song <= len(self.playlist):
            current_song_data = self.playlist[self.current_song - 1]  # -1 because we incremented already
            expected_duration = current_song_data['duration_sec']
            crossfade_info = current_song_data.get('debug_info', {}).get('cut', {})
            crossfade_duration = crossfade_info.get('crossfade_sec', 1.5)  # Default 1.5s
            
            log(f"Expected duration: {expected_duration:.1f}s, crossfade: {crossfade_duration:.1f}s")
            
            # Wait until it's time to start the crossfade
            crossfade_start_time = max(expected_duration - crossfade_duration, 1.0)  # At least 1 second
            log(f"Will start crossfade at {crossfade_start_time:.1f}s")
            
            # Sleep until crossfade time
            time.sleep(crossfade_start_time)
            
            # Start next song with crossfade if there is one
            if self.is_playing and self.current_song < len(self.playlist):
                log(f"Starting crossfade transition at {crossfade_start_time:.1f}s")
                print(f"\n🎛️ Starting crossfade transition ({crossfade_duration:.1f}s)...")
                print(f"   🔉 Current song fading out: {current_song_data['name']}")
                self.start_crossfade()
            
        # Wait for current song to finish
        log("Waiting for current audio process to finish...")
        start_time = time.time()
        self.current_process.wait()
        end_time = time.time()
        duration = end_time - start_time
        log(f"Audio process finished after {duration:.1f} seconds total")
        
        # Handle transition to next song
        if hasattr(self, 'next_process') and self.next_process:
            log("Completing crossfade transition")
            print("🎵 Crossfade complete - now playing next song")
            self.current_process = self.next_process
            self.next_process = None
            self.current_song += 1
            
            # Start monitoring the new current song
            if self.is_playing and self.current_song < len(self.playlist):
                threading.Thread(target=self.monitor_song, daemon=True).start()
        else:
            # No crossfade, just advance normally
            if self.is_playing and self.current_song < len(self.playlist):
                log("No crossfade - advancing to next song normally")
                print("\n🎵 Song finished! Moving to next...")
                self.play_next()
    
    def start_crossfade(self):
        """Start the next song with volume-controlled crossfade"""
        if not self.is_playing or self.current_song >= len(self.playlist):
            log("No crossfade needed - playlist ending")
            return
            
        next_song = self.playlist[self.current_song]
        crossfade_info = next_song.get('debug_info', {}).get('cut', {})
        crossfade_duration = crossfade_info.get('crossfade_sec', 1.5)
        
        log(f"Starting volume-controlled crossfade to: {next_song['name']}")
        
        audio_path = f"data/{next_song['song_id']}.mp3"
        log(f"Starting crossfade with volume control for: {audio_path}")
        
        print(f"   🔊 Fading in: {next_song['name']} (volume: 10% → 100%)")
        
        # Use sox to start at low volume and fade in
        # sox input.mp3 -t coreaudio default vol 0.1 fade t 0 0 1.5
        fade_in_time = min(crossfade_duration, 3.0)  # Max 3s fade
        
        try:
            # Start with low volume and fade in
            sox_cmd = [
                'sox', audio_path, '-t', 'coreaudio', 'default', '-q',  # -q for quiet
                'vol', '0.05',  # Start at 5% volume
                'fade', 't', str(fade_in_time), '0', '0'  # Fade in over crossfade duration
            ]
            log(f"Sox command: {' '.join(sox_cmd)}")
            next_process = subprocess.Popen(sox_cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            log(f"Volume-controlled crossfade started with PID: {next_process.pid}")
            
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            log(f"Sox failed ({e}), falling back to afplay")
            print(f"   🔊 Fading in: {next_song['name']} (using afplay)")
            next_process = subprocess.Popen(['afplay', audio_path])
        
        # Store the next process to replace current when crossfade completes
        self.next_process = next_process
    
    def stop_mix(self):
        """Stop current mix session"""
        self.is_playing = False
        if self.current_process:
            self.current_process.terminate()
        print("⏹️ Mix session stopped")

def main():
    """Main DJ interface"""
    dj = DJPlayer()
    
    print("🎧 Welcome to DJ MixAlgo!")
    print("=" * 40)
    dj.load_music()
    
    while True:
        print(f"\n🎛️ DJ Controls:")
        print("1. Start new mix")
        print("2. Play next song")
        print("3. Show playlist")
        print("4. Stop mix")
        print("0. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            length = input("Playlist length (default 10): ").strip()
            length = int(length) if length.isdigit() else 10
            dj.start_mix(length)
            
        elif choice == "2":
            if not dj.playlist:
                print("❌ Start a mix first.")
            else:
                dj.play_next()
                
        elif choice == "3":
            if not dj.playlist:
                print("❌ No playlist.")
            else:
                dj.show_playlist()
                
        elif choice == "4":
            dj.stop_mix()
                
        elif choice == "0":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()