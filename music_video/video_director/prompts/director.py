def get_global_plan_prompt(transcriptions_str, song_name):
    prompt = f"""
        You are a creative music video director. Your goal is to create a music video for the song {song_name}. 
        
        You are given a list of transcriptions of all 10-second segments of a song. You need to create a global plan for the entire music video.
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
        - No need to include timing or information about segments. Create the global plan for the entire video. 
        - From story to colors, to themes, to consistent visuals, to everything.

        The result of this will be used to generate snippet specific prompts for video generation, so make sure you generalize everything. 
        Make sure to use all the inforamtion in the transcriptions to create the gloabl plan. From music style, to instrtuments. 

        Try to make it intertesting and more story like. Make sure it is very likable, and meaningful. 
        BUILD OUT A CLEAR STORY TO BE THE MUSIC VIDEO FOR THE SONG. 
        """
        return prompt