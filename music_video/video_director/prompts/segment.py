def get_segment_prompt(prompt_data: dict):
    global_plan = prompt_data["global_plan"]
    all_video_prompts = prompt_data["all_video_prompts"]
    last_frame_path = prompt_data["last_frame_path"]
    transcription = prompt_data["transcription"]
    segment_index = prompt_data["segment_index"]
    song_name = prompt_data["song_name"]
    
    prompt = f"""
    You are a creative music video director. You are given a list of transcriptions of 10-second segments of a song. You need to create a global plan for the entire music video.
    The transcriptions are:
    {transcriptions_str}
    You need to create a global plan for the entire music video.
    The global plan should include:
    - Overall concept and theme
    - Narrative arc (if any)
    - Color palette and visual style
    - Recurring motifs and imagery
    - Transition rules and pacing
    - As much inforamtion as possible about the video plan
    - If there is a character in the video, we will provide the image of the artist. If you decide that no character is needed, you should say so.
    """

    return prompt