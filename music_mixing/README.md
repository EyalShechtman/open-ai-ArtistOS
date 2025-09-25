# Music Mixing System - Better Spotify DJ

An intelligent music mixing system that creates seamless playlists using algorithmic analysis and AI-powered song understanding. Unlike Spotify's DJ which relies on listening patterns, this system analyzes audio features and semantic content to make musically informed mixing decisions.

## Features

### 🎵 Smart Music Analysis
- **Audio Feature Extraction**: Tempo, MFCC, spectral centroid, chroma vectors, and energy analysis
- **AI-Powered Descriptions**: Qwen API generates detailed semantic analysis of each song
- **Multi-dimensional Compatibility**: Harmonic, tempo, timbre, and energy scoring for optimal transitions

### 🎛️ Intelligent Mixing Algorithm
- **Harmony Matching**: Chroma vector analysis for key/harmonic compatibility
- **Tempo Alignment**: BPM detection with intelligent warping (±12% max)
- **Timbre Continuity**: MFCC analysis for sound texture matching
- **Energy Flow**: Spectral centroid tracking for smooth intensity transitions
- **Semantic Tie-breaking**: AI descriptions ensure contextual appropriateness

### 🎧 DJ Interface
- **Automatic Playlists**: Generate seamless mixes with smooth crossfades
- **Real-time Playback**: CLI controls with volume-controlled transitions
- **History Management**: Prevents song repetition and maintains variety
- **Crossfade Planning**: 4-beat crossfades aligned to musical tempo

## Architecture

```
songs.json → Data Fetcher → MP3 Files → PreProcessor → processed_songs.csv → MixAlgo → Playlist
```

## Usage

### Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Prepare song metadata in `data/songs.json`
3. Run preprocessing: `python DJ/main.py`

### DJ Controls
```bash
python DJ/playlist.py
```
- Start new mix with automatic playlist generation
- Manual song advancement
- Real-time playlist management
- Crossfade monitoring and control

## Data Pipeline

### Input: `songs.json`
JSON array of song metadata with id, name, and artist fields.

### Processing Stages
1. **Download**: YouTube search → 40-second MP3 clips
2. **Feature Extraction**: Librosa analysis (tempo, MFCC, chroma, spectral features)
3. **AI Analysis**: Qwen API generates detailed song descriptions
4. **Database**: All features stored in `processed_songs.csv`

### Output
Seamlessly mixed playlists with calculated transition points and crossfade timings.

## Key Advantages Over Traditional DJs

- **Objective Analysis**: Mathematical scoring eliminates subjective bias
- **Semantic Understanding**: AI comprehends musical context and mood
- **Perfect Timing**: Sub-beat precision for seamless transitions
- **No Fatigue**: Algorithm never gets tired or makes inconsistent decisions
- **Scalable**: Analyzes entire music libraries instantly

## Technical Highlights

- **Robust Tempo Detection**: Beat tracking with silence trimming
- **Harmonic Compatibility**: 12-bin chroma vector cosine similarity
- **Energy Continuity**: Spectral centroid normalization and smoothing
- **Intelligent Prefiltering**: BPM tolerance with configurable warp limits
- **Memory Management**: Prevents repetition across long sessions

This system represents the future of algorithmic DJing, combining traditional audio engineering principles with modern AI capabilities to create mixes that rival human experts.
