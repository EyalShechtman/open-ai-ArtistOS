"""
Music Transcription Module

Uses Qwen's audio captioning model to generate text descriptions of music segments.
These descriptions capture instruments, mood, tempo, energy, and musical events.
"""

import sys
import os
import json

# Add parent directories to path to import QwenAPI
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from music_mixing.DJ.api import QwenAPI


class MusicTranscriber:
    """
    Transcribes audio segments into descriptive text using Qwen's API.
    
    The transcriptions describe musical characteristics like:
    - Instruments and sounds
    - Mood and atmosphere
    - Tempo and rhythm
    - Energy level and dynamics
    - Musical events (drops, breaks, fills, etc.)
    """
    
    def __init__(self):
        """Initialize the transcriber with QwenAPI client."""
        self.qwen = QwenAPI()
    
    def transcribe_segment(self, audio_path: str, save_to_file: bool = True) -> dict:
        """
        Transcribe a single audio segment to text.
        
        Args:
            audio_path: Path to the audio segment file
            save_to_file: If True, save transcription to ../music/transcriptions/ (default: True)
            
        Returns:
            Dictionary containing:
            - path: Path to the audio file
            - transcription: Text description of the music segment
            
        Example:
            transcriber = MusicTranscriber()
            result = transcriber.transcribe_segment("segment_0.mp3")
            # Returns: {
            #     "path": "segment_0.mp3",
            #     "transcription": "Upbeat electronic track with driving synths..."
            # }
            # Also saves to: ../music/transcriptions/songname_0.txt
        """
        print(f"Transcribing: {audio_path}")
        url = self.qwen.upload_temp_mp3(audio_path)
        qwen_result, _ = self.qwen.call_qwen(url)
        
        # Save transcription to file if requested
        if save_to_file:
            # Extract filename without extension (e.g., "HBP_0" from "HBP_0.mp3")
            filename_no_ext = os.path.splitext(os.path.basename(audio_path))[0]
            
            # Create transcriptions directory if it doesn't exist
            transcriptions_dir = os.path.join(os.path.dirname(__file__), '..', 'music', 'transcriptions')
            os.makedirs(transcriptions_dir, exist_ok=True)
            
            # Save transcription to text file
            output_file = os.path.join(transcriptions_dir, f"{filename_no_ext}.txt")
            with open(output_file, 'w') as f:
                f.write(qwen_result)
            print(f"Saved transcription to: {output_file}")
        
        return {"path": audio_path, "transcription": qwen_result}
    
    def transcribe_all_segments(self, segment_paths: list[str]) -> dict:
        """
        Transcribe multiple audio segments.
        
        Args:
            segment_paths: List of paths to audio segment files
            
        Returns:
            Dictionary mapping file paths to transcription results:
            {
                "segment_0.mp3": {"path": "...", "transcription": "..."},
                "segment_1.mp3": {"path": "...", "transcription": "..."}
            }
            
        Example:
            transcriber = MusicTranscriber()
            transcriptions = transcriber.transcribe_all_segments(segments)
        """
        transcriptions = {}
        for segment_path in segment_paths:
            transcription = self.transcribe_segment(segment_path)
            filename = os.path.basename(segment_path)
            transcriptions[filename] = transcription
        return transcriptions
    
if __name__ == "__main__":
    # Test with a single segment
    transcriber = MusicTranscriber()
    song_name = "HBP"
    segments_dir = "../music/segments"
    
    # Find the first segment to test
    test_file = f"{song_name}_0.mp3"
    test_path = os.path.join(segments_dir, test_file)
    
    if os.path.exists(test_path):
        print(f"Testing transcription with: {test_file}")
        result = transcriber.transcribe_segment(test_path)
        print("\nTranscription Result:")
        print(f"Path: {result['path']}")
        print(f"Transcription: {result['transcription']}")
    else:
        print(f"Error: Test file not found at {test_path}")
