# Music Video Director – Project Plan

## Objective
Create an agent-based system that automatically generates a full music video from an input song. The process breaks the song into 10-second segments, transcribes the audio into descriptions, and uses an AI director agent to plan and generate video snippets that are later assembled into a coherent, smoothly transitioning final video.

---

## High-Level Flow
1. **Input**
   - Provide an mp3 file as the source song.

2. **Segmentation**
   - Split the mp3 into fixed 10-second snippets.
   - Each snippet corresponds to a continuous video segment.

3. **Transcription**
   - For each snippet, call the Alibaba music transcription model.
   - The output is a text description of the music (instruments, mood, tempo, energy shifts, etc.).

4. **Global Director Plan**
   - The Director Agent ingests all snippet transcriptions.
   - It produces a global plan for the music video:
     - Overall concept
     - Theme and narrative arc
     - Color palette and visual style
     - Motifs and recurring imagery
     - Transition rules and pacing

5. **Snippet-Level Directives**
   - Starting with the first snippet:
     - Combine the snippet transcription with the global plan.
     - Generate a directive for the video generator (e.g., Veo3 or Kling).
   - For each subsequent snippet:
     - Use its transcription, the global director plan, and the **last frame** of the previous snippet.
     - possible picture of the main character in the video.
     - Generate a new directive ensuring **continuity** and **smooth transitions**.

6. **Video Generation**
   - Each directive is sent to the video model (Veo3 or Kling).
   - The model outputs a 10-second video clip.

7. **Assembly**
   - All clips are stitched together in sequence.
   - Transitions are smoothed (match cuts, fades, luma wipes, motion continuity).
   - Final audio (the original mp3) is overlaid.

8. **Final Output**
   - A coherent, artistically directed music video matching the full length of the song.

---

## Key Components
- **Transcription Module**  
  Uses Alibaba model to produce snippet-level music descriptions.

- **Director Agent (Global)**  
  Creates the global plan that defines the video’s theme, palette, motifs, style, and narrative arc.

- **Snippet Agent**  
  For each 10s snippet:
  - Uses the snippet’s transcription, global plan, and previous last frame.
  - Generates a snippet directive for the video model.

- **Video Generator**  
  Veo3 or Kling, limited to 10-second outputs.  
  Ensures directives are followed and continuity is respected.

- **Assembler**  
  Joins all snippets together, aligns with audio, and enforces transition smoothness.

---

## Transition Continuity Rules
- **Visual Continuity**: Maintain consistent palette, motifs, and style.  
- **Motion Continuity**: Match or deliberately invert motion vectors between clips.  
- **Frame Continuity**: Use the last frame of the previous snippet as a reference for the next.  
- **Beat Alignment**: Align cuts and effects with musical events (snare hits, drops, fills).  

---

## Deliverables
- **Global Director Plan**: Defines the entire video’s look and feel.  
- **Snippet Directives**: One per 10s segment, guiding video generation.  
- **Generated Clips**: 10-second video files.  
- **Final Assembly**: Complete music video with smooth transitions and original audio.  

---

## Summary
This system transforms a song into a directed music video through an agentic workflow:
- Song → Snippets → Transcriptions → Global Plan → Snippet Directives → Generated Clips → Final Assembly.  
The key innovation is the **Director Agent** that ensures both global coherence and snippet-to-snippet continuity.


```mermaid
flowchart TD
    A[Input Song (mp3)] --> B[Split into 10s Snippets]
    B --> C[Alibaba Transcriber<br/>(Music → Text)]
    C --> D[Director Agent<br/>(Global Plan)]
    D --> E1[Snippet Agent<br/>for Snippet 1]
    E1 --> F1[Veo3 / Kling<br/>Generate Clip 1]
    F1 --> G[Assembler]

    D --> E2[Snippet Agent<br/>for Snippet 2+]
    F1 --> E2
    E2 --> F2[Veo3 / Kling<br/>Generate Clip 2]
    F2 --> G

    G --> H[Final Music Video<br/>with Smooth Transitions]
