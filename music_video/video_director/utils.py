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
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")
    
    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Set position to last frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
    
    # Read the last frame
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        raise ValueError(f"Could not read last frame from video: {video_path}")
    
    # Determine output path if not provided
    if output_path is None:
        # Create frames directory in music folder
        base_dir = os.path.join(os.path.dirname(__file__), '..', 'music', 'frames')
        os.makedirs(base_dir, exist_ok=True)
        
        # Extract song name and index from video filename (e.g., "HBP_0.mp4" -> "HBP_0_last.jpg")
        filename = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(base_dir, f"{filename}_last.jpg")
    
    # Save the frame
    cv2.imwrite(output_path, frame)
    print(f"Extracted last frame to: {output_path}")
    
    return output_path


def create_output_directories(base_dir: str) -> dict:
    """
    Create organized output directory structure.
    
    Args:
        base_dir: Base directory for all outputs (typically ../music/)
        
    Returns:
        Dictionary with paths to subdirectories:
        - songs: Original song files
        - segments: Audio segments
        - transcriptions: Transcription text files
        - global_plan: Global video plan
        - video_prompts: Video prompts for each segment
        - videos: Generated video clips
        - frames: Extracted frames for continuity
        
    Example:
        dirs = create_output_directories("../music")
    """
    directories = {
        'songs': os.path.join(base_dir, 'songs'),
        'segments': os.path.join(base_dir, 'segments'),
        'transcriptions': os.path.join(base_dir, 'transcriptions'),
        'global_plan': os.path.join(base_dir, 'global_plan'),
        'video_prompts': os.path.join(base_dir, 'video_prompts'),
        'videos': os.path.join(base_dir, 'videos'),
        'frames': os.path.join(base_dir, 'frames')
    }
    
    # Create all directories
    for dir_path in directories.values():
        os.makedirs(dir_path, exist_ok=True)
    
    return directories
