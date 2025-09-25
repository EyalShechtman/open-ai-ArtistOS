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
from api import QwenAPI

def log(message, level="INFO"):
    """Log with timestamp and level"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

class DJPlayer:
    def __init__(self):
        self.algo = MixAlgo()
        self.current_song = 0
        self.playlist = []
        self.is_playing = False
        self.current_process = None
        self.next_process = None
        self.qwen_api = QwenAPI()
        self.monitor_thread = None  # Track current monitor thread
        self.manual_mode = False  # Track if user is manually controlling playback

    def load_music(self):
        """Load music data and initialize algorithm"""
        log("load_music() called", "METHOD")
        print("🎵 Loading music library...")
        df = pd.read_csv("processed_songs.csv")
        log(f"Loaded DataFrame with {len(df)} rows and columns: {list(df.columns)}", "DATA")

        # Compute text embeddings for semantic tie-breaking
        embeddings = {}
        print("🧠 Computing text embeddings...")
        for _, row in df.iterrows():
            song_id = str(row['id'])
            qwen_text = row.get('qwen_analysis', '')
            if qwen_text:
                embedding = self.qwen_api.get_text_embedding(qwen_text)
                if embedding:
                    embeddings[song_id] = embedding
                    log(f"Embedded song {song_id}: {row['name'][:30]}", "EMBED")
                else:
                    log(f"Failed to embed song {song_id}", "WARN")
            else:
                log(f"No text for song {song_id}", "WARN")

        log(f"Computed {len(embeddings)} embeddings out of {len(df)} songs", "DATA")

        # Fit the algorithm with embeddings
        self.algo.fit(df, embeddings=embeddings)
        log(f"MixAlgo fit completed, by_id keys: {len(self.algo.by_id)}", "DATA")
        print(f"✅ Loaded {len(df)} songs with {len(embeddings)} embeddings")
        
    def start_mix(self, playlist_length=10):
        """Start a new mix session"""
        log(f"start_mix() called with length={playlist_length}", "METHOD")
        available_songs = list(self.algo.by_id.keys())
        log(f"Available songs count: {len(available_songs)}", "DATA")

        start_song_id = random.choice(available_songs)
        log(f"Selected starting song: {start_song_id}", "DECISION")

        print(f"\n🎧 Starting mix session...")
        log("Calling algo.generate_playlist()", "CALL")
        self.playlist = self.algo.generate_playlist(start_song_id, playlist_length)
        log(f"generate_playlist returned {len(self.playlist)} songs", "RESULT")

        self.current_song = 0
        self.is_playing = True
        log(f"Set state: current_song={self.current_song}, is_playing={self.is_playing}", "STATE")

        print(f"Generated {len(self.playlist)} song playlist")
        self.show_playlist()
        # Auto-start playback
        if self.playlist:
            self.play_next()
        
    def show_playlist(self):
        """Display current playlist"""
        print(f"\n📋 Current Playlist:")
        for i, song in enumerate(self.playlist):
            marker = "▶️" if i == self.current_song else "  "
            print(f"{marker} {i+1}. {song['name']} by {song['artist']} ({song['tempo_bpm']:.1f} BPM)")
    
    def play_next(self):
        """Play next song in playlist"""
        log(f"play_next() called - current_song={self.current_song}, playlist_length={len(self.playlist)}, is_playing={self.is_playing}", "METHOD")

        if not self.is_playing or self.current_song >= len(self.playlist):
            log("Playlist complete or not playing - stopping", "DECISION")
            print("🎉 Playlist complete!")
            self.is_playing = False
            return

        # Set manual control flag to prevent automatic crossfades
        self.manual_mode = True
            
        song = self.playlist[self.current_song]
        log(f"Playing song {self.current_song + 1}: {song['name']}")
        print(f"\n🎵 Now Playing: {song['name']} by {song['artist']}")
        
        # Stop current audio and monitor thread
        if self.current_process:
            log("Terminating previous audio process")
            self.current_process.terminate()

        # Stop current monitor thread if it exists
        if self.monitor_thread and self.monitor_thread.is_alive():
            log("Stopping previous monitor thread")
            # Note: daemon threads will be terminated when main thread exits

        # Play new song
        audio_path = f"data/{song['song_id']}.mp3"
        log(f"Starting audio process for: {audio_path}")
        print(f"   🎵 Playing: {audio_path}")

        # Require sox for proper volume control and crossfading
        # Current song plays at full volume - crossfading is handled separately
        sox_cmd = ['sox', audio_path, '-t', 'coreaudio', 'default', '-q']

        self.current_process = subprocess.Popen(sox_cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        log(f"Sox audio process started with PID: {self.current_process.pid}")

        # Start monitoring for when song ends
        log("Starting monitor thread")
        self.monitor_thread = threading.Thread(target=self.monitor_song, daemon=True)
        self.monitor_thread.start()
        log(f"Monitor thread started: {self.monitor_thread.name}")
        
        self.current_song += 1
        log(f"Incremented current_song to: {self.current_song}")
    
    def monitor_song(self):
        """Monitor current song and handle crossfade transition"""
        log(f"monitor_song() started - PID: {self.current_process.pid if self.current_process else 'None'}", "METHOD")

        if not self.current_process:
            log("No current process to monitor", "ERROR")
            return

        # Store the song index this monitor was created for
        monitor_song_index = self.current_song - 1  # The song that was just started

        # Get crossfade timing from the cut info for the transition to next song
        if monitor_song_index >= 0 and monitor_song_index + 1 < len(self.playlist):
            current_song_data = self.playlist[monitor_song_index]  # Song this monitor is for
            next_song_data = self.playlist[monitor_song_index + 1]  # Next song to transition to

            # Get cut info for the transition from current to next
            cut_info = next_song_data.get('debug_info', {}).get('cut', {})
            crossfade_start_time = cut_info.get('A_out_time_sec', 30.0)  # When to start crossfade
            crossfade_duration = cut_info.get('crossfade_sec', 2.0)  # How long crossfade lasts

            log(f"Crossfade timing: start at {crossfade_start_time:.1f}s, duration {crossfade_duration:.1f}s", "TIMING")
            log(f"Monitor for song: {current_song_data['name']}, Next: {next_song_data['name']}", "DATA")

            # Sleep until it's time to start the crossfade
            log(f"Sleeping for {crossfade_start_time:.1f}s until crossfade time", "TIMING")
            time.sleep(crossfade_start_time)

            # Check if this monitor is still relevant (song hasn't been manually advanced)
            if self.is_playing and self.current_song == monitor_song_index + 1 and not getattr(self, 'manual_mode', False):
                log(f"Starting crossfade transition at {crossfade_start_time:.1f}s", "ACTION")
                print(f"\n🎛️ Starting crossfade transition ({crossfade_duration:.1f}s)...")
                print(f"   🔉 Current: {current_song_data['name']}")
                print(f"   🔊 Next: {next_song_data['name']}")
                log("Calling start_crossfade()", "CALL")
                self.start_crossfade(monitor_song_index + 1)  # Pass the correct next song index
            else:
                reason = "manual mode active" if getattr(self, 'manual_mode', False) else "song was manually advanced or stopped"
                log(f"Skipping crossfade - {reason}", "DECISION")
            
        # Wait for current song to finish
        log("Waiting for current audio process to finish...")
        start_time = time.time()
        self.current_process.wait()
        end_time = time.time()
        duration = end_time - start_time
        log(f"Audio process finished after {duration:.1f} seconds total")

        # Only auto-advance if not in manual mode
        if not getattr(self, 'manual_mode', False):
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
        else:
            log("In manual mode - not auto-advancing", "DECISION")
    
    def start_crossfade(self, next_song_index=None):
        """Start the next song with volume-controlled crossfade"""
        log("start_crossfade() called", "METHOD")

        if not self.is_playing:
            log("Not playing - skipping crossfade", "DECISION")
            return

        # Use provided index or default to current_song
        if next_song_index is None:
            next_song_index = self.current_song

        if next_song_index >= len(self.playlist):
            log("No crossfade needed - playlist ending", "DECISION")
            return

        next_song = self.playlist[next_song_index]
        cut_info = next_song.get('debug_info', {}).get('cut', {})
        crossfade_duration = cut_info.get('crossfade_sec', 2.0)

        log(f"Starting volume-controlled crossfade to: {next_song['name']}", "ACTION")
        log(f"Crossfade duration: {crossfade_duration:.3f}s", "DATA")

        audio_path = f"data/{next_song['song_id']}.mp3"
        log(f"Starting crossfade with volume control for: {audio_path}", "AUDIO")

        print(f"   🔊 Fading in: {next_song['name']} (0% → 100% in {crossfade_duration:.1f}s)")

        # Use sox to fade in from silence to full volume over the crossfade duration
        sox_cmd = [
            'sox', audio_path, '-t', 'coreaudio', 'default', '-q',  # -q for quiet
            'fade', 't', f"{crossfade_duration:.6f}", '0', '0'  # fade type t: fade in over crossfade_duration
        ]
        log(f"Sox command: {' '.join(sox_cmd)}")
        next_process = subprocess.Popen(sox_cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        log(f"Volume-controlled crossfade started with PID: {next_process.pid}")

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
    log("main() called - starting DJ MixAlgo", "MAIN")

    dj = DJPlayer()
    log("DJPlayer instance created", "INIT")

    print("🎧 Welcome to DJ MixAlgo!")
    print("=" * 40)
    log("Calling dj.load_music()", "CALL")
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