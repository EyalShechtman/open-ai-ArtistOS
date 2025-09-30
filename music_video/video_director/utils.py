"""
Utility Functions

Helper functions for frame extraction, file management, and video processing.
"""

import os
import cv2


def extract_last_frame(video_path: str, output_path: str = None) -> str:
    """
    Extract the last frame from a video file.
    
    This frame is used as a reference for the next segment to ensure visual continuity.
    
    Args:
        video_path: Path to the video file
        output_path: Where to save the extracted frame (defaults to video_path with .jpg extension)
        
    Returns:
        Path to the saved frame image
        
    Example:
        last_frame = extract_last_frame("segment_0.mp4", "frame_0_last.jpg")
    """
    # TODO: Implement this function
    # Steps:
    # 1. Open video with OpenCV
    # 2. Seek to the last frame
    # 3. Extract and save as image
    # 4. Return output path
    pass


def create_output_directories(base_dir: str) -> dict:
    """
    Create organized output directory structure.
    
    Args:
        base_dir: Base directory for all outputs
        
    Returns:
        Dictionary with paths to subdirectories:
        - segments: Audio segments
        - transcriptions: Transcription JSON files
        - frames: Extracted frames
        - videos: Generated video clips
        - final: Final assembled video
        
    Example:
        dirs = create_output_directories("output/my_video")
    """
    # TODO: Implement this function
    pass
