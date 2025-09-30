"""
Music Video Director - Agent-based system for automatic music video generation

Components:
- audio_processor: Splits audio into 10-second segments
- transcriber: Converts audio segments to text descriptions using Qwen
- director_agent: Creates global video plan and snippet directives
- video_generator: Interfaces with Veo3 API for video generation
- assembler: Stitches video clips together with smooth transitions
- utils: Helper functions for frame extraction and file management
"""
