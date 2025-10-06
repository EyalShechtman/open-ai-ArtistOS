"""
Audio Processing Module

Handles splitting input songs into fixed-duration segments for video generation.
Each segment will be transcribed and used to generate a corresponding video clip.
"""

import os
from pydub import AudioSegment


class AudioProcessor:
    """
    Splits audio files into fixed-duration segments.
    
    Default segment length is 10 seconds to match video generation constraints.
    """
    
    def __init__(self, segment_duration: int = 8):
        """
        Initialize the audio processor.
        
        Args:
            segment_duration: Duration of each segment in seconds (default: 10)
        """
        self.segment_duration = segment_duration * 1000  # Convert to milliseconds
    
    def split_audio(self, input_path: str, output_dir: str) -> list[str]:
        """
        Split an audio file into fixed-duration segments.
        
        Args:
            input_path: Path to the input mp3 file
            output_dir: Directory to save the segment files
            
        Returns:
            List of paths to the generated segment files, in order
            
        Example:
            processor = AudioProcessor(segment_duration=10)
            segments = processor.split_audio("song.mp3", "output/segments")
            # Returns: ["output/segments/segment_0.mp3", "output/segments/segment_1.mp3", ...]
        """
        # 1. Load the audio file using pydub
        audio = AudioSegment.from_mp3(input_path)
        
        # 2. Calculate number of segments needed
        total_duration = len(audio)  # Duration in milliseconds
        num_segments = (total_duration + self.segment_duration - 1) // self.segment_duration  # Ceiling division
        
        # 3. Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # 4. Extract song name from input path
        song_name = os.path.splitext(os.path.basename(input_path))[0]
        
        # 5. Split audio into segments and save with sequential naming
        output_paths = []
        for i in range(num_segments):
            start_time = i * self.segment_duration
            end_time = min((i + 1) * self.segment_duration, total_duration)
            
            # Extract segment
            segment = audio[start_time:end_time]
            
            # Create output filename: songName_N.mp3
            output_filename = f"{song_name}_{i}.mp3"
            output_path = os.path.join(output_dir, output_filename)
            
            # Export segment
            segment.export(output_path, format="mp3")
            output_paths.append(output_path)
            
            print(f"Created segment {i + 1}/{num_segments}: {output_filename}")
        
        # 6. Return list of output paths
        return output_paths


if __name__ == "__main__":
    processor = AudioProcessor(segment_duration=8)
    processor.split_audio("../music/songs/HBP.mp3", "../music/segments")