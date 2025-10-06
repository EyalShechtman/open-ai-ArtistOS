"""
Director Agent Module

Creates global video plans and per-snippet directives for video generation.
The Director Agent ensures visual coherence and narrative flow across the entire video.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts.director import get_global_plan_prompt
from prompts.segment import get_segment_prompt

load_dotenv()


class DirectorAgent:
    """
    AI-powered director that plans music videos.
    
    Responsibilities:
    1. Create a global plan defining the video's overall aesthetic
    2. Generate snippet-level directives that maintain continuity
    """
    
    def __init__(self, model: str = "gemini-2.5-pro"):
        """
        Initialize the director agent.
        
        Args:
            model: Gemini model to use for planning (default: gemini-2.0-flash-exp)
        """
        self.client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.model = model
        self.global_plan = None
        self.all_video_prompts = []
    def create_global_plan(self, transcriptions: list[dict], song_name: str = "HBP") -> dict:
        """
        Create a global plan for the entire music video.
        
        Analyzes all music transcriptions to define:
        - Overall concept and theme
        - Narrative arc (if any)
        - Color palette and visual style
        - Recurring motifs and imagery
        - Transition rules and pacing
        
        Args:
            transcriptions: List of segment transcriptions from MusicTranscriber
            song_name: Name of the song (used for saving the plan file)
            
        Returns:
            Dictionary containing the global plan with keys:
            - concept: Overall video concept
            - theme: Thematic elements
            - style: Visual style and aesthetics
            - palette: Color palette description
            - motifs: Recurring visual elements
            - transitions: Rules for transitions between segments
            
        Example:
            director = DirectorAgent()
            plan = director.create_global_plan(transcriptions, song_name="HBP")
        """
        transcriptions_str = ""
        for transcription in transcriptions:
            transcriptions_str += f"{transcription['path']}: {transcription['transcription']}\n"
        prompt = get_global_plan_prompt(transcriptions_str, song_name)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        global_plan_content = response.choices[0].message.content
        self.global_plan = global_plan_content
        
        # Save global plan to file: music/global_plan/{songname}.txt
        global_plan_dir = os.path.join(os.path.dirname(__file__), '..', 'music', 'global_plan')
        os.makedirs(global_plan_dir, exist_ok=True)
        
        output_path = os.path.join(global_plan_dir, f"{song_name}.txt")
        with open(output_path, 'w') as f:
            f.write(global_plan_content)
        print(f"Saved global plan to: {output_path}")
        
        return global_plan_content
    
    def generate_snippet_directive(
        self, 
        song_name: str,
        segment_index: int
    ) -> str:
        """
        Generate a video generation directive for a single snippet.
        
        This function automatically loads everything from music/ directory:
        - Transcription from music/transcriptions/{song_name}_{index}.txt
        - Global plan from music/global_plan/{song_name}.txt
        - Previous frame from music/frames/{song_name}_{index-1}_last.jpg (if exists)
        - All previous video prompts from music/video_prompts/{song_name}_*.txt
        
        Args:
            song_name: Name of the song (used to find all files)
            segment_index: Index of the current segment (0, 1, 2, ...)
            
        Returns:
            Directive string to send to video generation API
            
        Example:
            director = DirectorAgent()
            # Everything is automatically loaded from music/ directory
            directive = director.generate_snippet_directive(
                song_name="HBP",
                segment_index=0
            )
        """
        music_dir = os.path.join(os.path.dirname(__file__), '..', 'music')
        
        # 1. Load transcription from music/transcriptions/{song_name}_{index}.txt
        transcription_path = os.path.join(music_dir, 'transcriptions', f"{song_name}_{segment_index}.txt")
        with open(transcription_path, 'r') as f:
            transcription = f.read().strip()
        
        # 2. Load global plan from music/global_plan/{song_name}.txt
        global_plan_path = os.path.join(music_dir, 'global_plan', f"{song_name}.txt")
        with open(global_plan_path, 'r') as f:
            global_plan = f.read().strip()
        
        # 3. Load previous frame if this is not the first segment
        previous_frame_path = None
        if segment_index > 0:
            previous_frame_path = os.path.join(music_dir, 'frames', f"{song_name}_{segment_index - 1}_last.jpg")
            if not os.path.exists(previous_frame_path):
                previous_frame_path = None  # Frame doesn't exist yet
        
        # 4. Load all previous video prompts from music/video_prompts/
        all_video_prompts = []
        for i in range(segment_index):
            prompt_path = os.path.join(music_dir, 'video_prompts', f"{song_name}_{i}.txt")
            if os.path.exists(prompt_path):
                with open(prompt_path, 'r') as f:
                    all_video_prompts.append(f.read().strip())
        
        # Format all previous video prompts with their indexes
        previous_prompts_str = ""
        if all_video_prompts:
            for i, prompt in enumerate(all_video_prompts):
                previous_prompts_str += f"Segment {i}: {prompt}\n\n"
        else:
            previous_prompts_str = "This is the first segment of the video."
        
        # Build the prompt data structure that will be sent to Gemini
        prompt_data = {
            "global_plan": global_plan,
            "all_video_prompts": previous_prompts_str,
            "last_frame_path": previous_frame_path if previous_frame_path else "No previous frame (this is the first segment)",
            "transcription": transcription,
            "segment_index": segment_index,
            "song_name": song_name
        }
        
        # TODO: Call Gemini API with this data to generate video directive
        # For now, return formatted string showing all loaded data
        video_prompt = f"""
                        === VIDEO DIRECTIVE DATA FOR {song_name} - SEGMENT {segment_index} ===

                        📝 TRANSCRIPTION:
                        {transcription}

                        🎬 GLOBAL PLAN:
                        {global_plan}

                        🎞️ PREVIOUS VIDEO PROMPTS:
                        {previous_prompts_str}

                        🖼️ LAST FRAME PATH:
                        {previous_frame_path if previous_frame_path else "No previous frame (this is the first segment)"}

                        📊 METADATA:
                        - Song: {song_name}
                        - Segment Index: {segment_index}
                        - Number of previous prompts: {len(all_video_prompts)}

                        === END OF DATA ===
                        """
        
        # Save video prompt to music/video_prompts/{song_name}_{index}.txt
        video_prompts_dir = os.path.join(music_dir, 'video_prompts')
        os.makedirs(video_prompts_dir, exist_ok=True)
        
        output_path = os.path.join(video_prompts_dir, f"{song_name}_{segment_index}.txt")
        with open(output_path, 'w') as f:
            f.write(video_prompt)
        print(f"✅ Saved video prompt to: {output_path}")
        
        return video_prompt




if __name__ == "__main__":
    director = DirectorAgent()
    
    # Load transcriptions from music/transcriptions/
    music_dir = os.path.join(os.path.dirname(__file__), '..', 'music')
    transcriptions_dir = os.path.join(music_dir, 'transcriptions')
    
    # Get all transcription files for HBP
    transcriptions = []
    song_name = "HBP"
    segment_index = 0
    
    # Load HBP_0.txt
    transcription_path = os.path.join(transcriptions_dir, f"{song_name}_{segment_index}.txt")
    if os.path.exists(transcription_path):
        with open(transcription_path, 'r') as f:
            transcription_text = f.read().strip()
            transcriptions.append({
                "segment_index": segment_index,
                "path": f"{song_name}_{segment_index}.mp3",
                "transcription": transcription_text
            })
        print(f"✅ Loaded transcription for segment {segment_index}")
    
    # Test 1: Create global plan
    print("\n=== TEST 1: Creating Global Plan ===")
    global_plan = director.create_global_plan(transcriptions, song_name=song_name)
    print(f"Global plan created and saved!")
    
    # Test 2: Generate snippet directive
    print("\n=== TEST 2: Generating Snippet Directive ===")
    result = director.generate_snippet_directive(song_name=song_name, segment_index=0)
    print(result)

