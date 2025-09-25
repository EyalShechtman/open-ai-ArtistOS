#!/usr/bin/env python3
"""
Reason Codes Generator for Music Mixing System

This script analyzes the scoring system and generates detailed explanations
for each song's compatibility scores and mixing decisions.

Author: AI Assistant
Date: 2024
"""

import os
import json
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import math

class ReasonCodesGenerator:
    """
    Generates detailed reason codes and explanations for music mixing decisions.
    """
    
    def __init__(self, csv_path: str = "processed_songs.csv"):
        self.csv_path = csv_path
        self.df = None
        self.by_id = {}
        self.energy_scale = 1.0
        self.load_data()
        
    def load_data(self):
        """Load and prepare the processed songs data."""
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
            
        self.df = pd.read_csv(self.csv_path)
        
        # Parse chroma vectors from JSON strings
        import json
        for col in ("first_chroma_vec_12", "last_chroma_vec_12"):
            if col in self.df.columns:
                def parse_chroma(v):
                    if isinstance(v, (list, tuple, np.ndarray)):
                        return np.asarray(v, float)
                    elif isinstance(v, str):
                        try:
                            parsed = json.loads(v)
                            return np.asarray(parsed, float)
                        except (json.JSONDecodeError, ValueError):
                            return np.nan
                    else:
                        return np.nan
                self.df[col] = self.df[col].apply(parse_chroma)
        
        # Build ID index
        self.by_id = {str(r["id"]): r for _, r in self.df.iterrows()}
        
        # Calculate energy scale for continuity normalization
        if "centroid_mean" in self.df.columns:
            vals = self.df["centroid_mean"].dropna().to_numpy()
            if len(vals) >= 5:
                mad = np.median(np.abs(vals - np.median(vals))) + 1e-9
                self.energy_scale = 6 * mad
            else:
                self.energy_scale = max(1.0, np.std(vals) + 1e-9)
    
    def analyze_harmonic_compatibility(self, song_a: pd.Series, song_b: pd.Series) -> Dict:
        """
        Analyze harmonic compatibility between two songs.
        Returns detailed analysis of chroma vector similarity.
        """
        a_chroma = song_a.get("last_chroma_vec_12", None)
        b_chroma = song_b.get("first_chroma_vec_12", None)
        
        if not (isinstance(a_chroma, np.ndarray) and isinstance(b_chroma, np.ndarray)):
            return {
                "score": 0.0,
                "reason": "Missing chroma vectors",
                "details": "Cannot compute harmonic compatibility without chroma data"
            }
        
        # Calculate cosine similarity
        cos_sim = self._cosine_similarity(a_chroma, b_chroma)
        score = 0.5 * (1.0 + cos_sim)  # Map to [0,1]
        
        # Analyze chroma patterns
        a_peaks = np.argsort(a_chroma)[-3:]  # Top 3 notes
        b_peaks = np.argsort(b_chroma)[-3:]
        
        # Check for common notes
        common_notes = set(a_peaks) & set(b_peaks)
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        details = {
            "cosine_similarity": float(cos_sim),
            "mapped_score": float(score),
            "song_a_strongest_notes": [note_names[i] for i in a_peaks],
            "song_b_strongest_notes": [note_names[i] for i in b_peaks],
            "common_notes": [note_names[i] for i in common_notes],
            "harmonic_relationship": self._get_harmonic_relationship(cos_sim)
        }
        
        if score > 0.8:
            reason = "Excellent harmonic match - very similar chord progressions"
        elif score > 0.6:
            reason = "Good harmonic compatibility - some shared tonal elements"
        elif score > 0.4:
            reason = "Moderate harmonic compatibility - different but complementary"
        else:
            reason = "Poor harmonic match - very different tonal characteristics"
            
        return {
            "score": score,
            "reason": reason,
            "details": details
        }
    
    def analyze_tempo_compatibility(self, song_a: pd.Series, song_b: pd.Series) -> Dict:
        """
        Analyze tempo compatibility between two songs.
        """
        a_tempo = float(song_a["tempo_bpm"])
        b_tempo = float(song_b["tempo_bpm"])
        
        # Calculate absolute and relative differences
        abs_diff = abs(a_tempo - b_tempo)
        rel_diff = abs_diff / max(a_tempo, b_tempo, 1e-6)
        
        # Calculate tempo score (same as MixAlgo)
        bpm_tol = 6.0
        max_warp = 0.12
        
        base_score = math.exp(-(abs_diff / bpm_tol) ** 2)
        if rel_diff <= max_warp:
            score = base_score
        else:
            score = 0.5 * base_score
        
        # Determine tempo relationship
        if abs_diff <= 2:
            tempo_relationship = "Perfect match"
        elif abs_diff <= 5:
            tempo_relationship = "Very close"
        elif abs_diff <= 10:
            tempo_relationship = "Close"
        elif abs_diff <= 20:
            tempo_relationship = "Moderate difference"
        else:
            tempo_relationship = "Large difference"
        
        # Check if songs are in compatible tempo ranges
        tempo_ranges = {
            "very_slow": (60, 80),
            "slow": (80, 100),
            "moderate": (100, 120),
            "fast": (120, 140),
            "very_fast": (140, 180)
        }
        
        a_range = self._get_tempo_range(a_tempo, tempo_ranges)
        b_range = self._get_tempo_range(b_tempo, tempo_ranges)
        
        details = {
            "song_a_tempo": a_tempo,
            "song_b_tempo": b_tempo,
            "absolute_difference": abs_diff,
            "relative_difference": rel_diff,
            "tempo_relationship": tempo_relationship,
            "song_a_range": a_range,
            "song_b_range": b_range,
            "compatible_ranges": a_range == b_range,
            "warp_required": rel_diff > max_warp
        }
        
        if score > 0.9:
            reason = f"Excellent tempo match ({a_tempo:.1f} → {b_tempo:.1f} BPM)"
        elif score > 0.7:
            reason = f"Good tempo compatibility ({a_tempo:.1f} → {b_tempo:.1f} BPM)"
        elif score > 0.5:
            reason = f"Moderate tempo difference ({a_tempo:.1f} → {b_tempo:.1f} BPM)"
        else:
            reason = f"Poor tempo match ({a_tempo:.1f} → {b_tempo:.1f} BPM) - may need significant warping"
            
        return {
            "score": score,
            "reason": reason,
            "details": details
        }
    
    def analyze_timbre_compatibility(self, song_a: pd.Series, song_b: pd.Series) -> Dict:
        """
        Analyze timbre compatibility based on MFCC and spectral features.
        """
        # Extract feature vectors (same as MixAlgo)
        vec_a = np.array([
            float(song_a["mfcc_mean"]),
            float(song_a["mfcc_std"]),
            float(song_a["centroid_mean"])
        ])
        vec_b = np.array([
            float(song_b["mfcc_mean"]),
            float(song_b["mfcc_std"]),
            float(song_b["centroid_mean"])
        ])
        
        # Calculate distance and score
        distance = np.linalg.norm(vec_a - vec_b)
        score = 1.0 / (1.0 + distance)
        
        # Analyze individual components
        mfcc_mean_diff = abs(vec_a[0] - vec_b[0])
        mfcc_std_diff = abs(vec_a[1] - vec_b[1])
        centroid_diff = abs(vec_a[2] - vec_b[2])
        
        # Interpret MFCC differences
        mfcc_mean_interpretation = self._interpret_mfcc_mean_diff(mfcc_mean_diff)
        mfcc_std_interpretation = self._interpret_mfcc_std_diff(mfcc_std_diff)
        centroid_interpretation = self._interpret_centroid_diff(centroid_diff)
        
        details = {
            "mfcc_mean_a": float(vec_a[0]),
            "mfcc_mean_b": float(vec_b[0]),
            "mfcc_std_a": float(vec_a[1]),
            "mfcc_std_b": float(vec_b[1]),
            "centroid_a": float(vec_a[2]),
            "centroid_b": float(vec_b[2]),
            "mfcc_mean_difference": mfcc_mean_diff,
            "mfcc_std_difference": mfcc_std_diff,
            "centroid_difference": centroid_diff,
            "euclidean_distance": distance,
            "mfcc_mean_interpretation": mfcc_mean_interpretation,
            "mfcc_std_interpretation": mfcc_std_interpretation,
            "centroid_interpretation": centroid_interpretation
        }
        
        if score > 0.8:
            reason = "Excellent timbre match - very similar spectral characteristics"
        elif score > 0.6:
            reason = "Good timbre compatibility - similar sound textures"
        elif score > 0.4:
            reason = "Moderate timbre difference - complementary but distinct"
        else:
            reason = "Poor timbre match - very different spectral characteristics"
            
        return {
            "score": score,
            "reason": reason,
            "details": details
        }
    
    def analyze_energy_compatibility(self, song_a: pd.Series, song_b: pd.Series) -> Dict:
        """
        Analyze energy continuity between songs.
        """
        # Get energy values (same as MixAlgo)
        a_energy = float(song_a.get("last_slice_centroid_mean", song_a.get("centroid_mean", 0.0)))
        b_energy = float(song_b.get("first_slice_centroid_mean", song_b.get("centroid_mean", 0.0)))
        
        # Calculate score
        energy_diff = abs(a_energy - b_energy)
        score = 1 - min(1.0, energy_diff / self.energy_scale)
        
        # Determine energy relationship
        energy_ratio = b_energy / max(a_energy, 1e-6)
        
        if energy_ratio > 1.2:
            energy_transition = "Energy increase"
        elif energy_ratio > 0.8:
            energy_transition = "Energy maintenance"
        else:
            energy_transition = "Energy decrease"
        
        # Categorize energy levels
        a_energy_level = self._categorize_energy(a_energy)
        b_energy_level = self._categorize_energy(b_energy)
        
        details = {
            "song_a_energy": a_energy,
            "song_b_energy": b_energy,
            "energy_difference": energy_diff,
            "energy_ratio": energy_ratio,
            "energy_transition": energy_transition,
            "song_a_energy_level": a_energy_level,
            "song_b_energy_level": b_energy_level,
            "energy_scale": self.energy_scale,
            "normalized_difference": energy_diff / self.energy_scale
        }
        
        if score > 0.8:
            reason = f"Excellent energy continuity ({a_energy:.0f} → {b_energy:.0f} Hz)"
        elif score > 0.6:
            reason = f"Good energy flow ({a_energy:.0f} → {b_energy:.0f} Hz)"
        elif score > 0.4:
            reason = f"Moderate energy change ({a_energy:.0f} → {b_energy:.0f} Hz)"
        else:
            reason = f"Poor energy continuity ({a_energy:.0f} → {b_energy:.0f} Hz) - may cause jarring transition"
            
        return {
            "score": score,
            "reason": reason,
            "details": details
        }
    
    def generate_song_analysis(self, song_id: str) -> Dict:
        """
        Generate comprehensive analysis for a single song.
        """
        if song_id not in self.by_id:
            return {"error": f"Song {song_id} not found"}
        
        song = self.by_id[song_id]
        
        # Basic song info
        analysis = {
            "song_id": song_id,
            "name": song["name"],
            "artist": song["artist"],
            "duration_sec": song["duration_sec"],
            "tempo_bpm": song["tempo_bpm"],
            "analysis_timestamp": datetime.now().isoformat(),
            "compatibility_scores": {}
        }
        
        # Analyze compatibility with all other songs
        for other_id, other_song in self.by_id.items():
            if other_id == song_id:
                continue
                
            compatibility = {
                "harmonic": self.analyze_harmonic_compatibility(song, other_song),
                "tempo": self.analyze_tempo_compatibility(song, other_song),
                "timbre": self.analyze_timbre_compatibility(song, other_song),
                "energy": self.analyze_energy_compatibility(song, other_song)
            }
            
            # Calculate overall score (same weights as MixAlgo)
            weights = {"harm": 0.40, "tempo": 0.25, "timbre": 0.20, "energy": 0.15}
            overall_score = (
                weights["harm"] * compatibility["harmonic"]["score"] +
                weights["tempo"] * compatibility["tempo"]["score"] +
                weights["timbre"] * compatibility["timbre"]["score"] +
                weights["energy"] * compatibility["energy"]["score"]
            )
            
            compatibility["overall_score"] = overall_score
            compatibility["overall_reason"] = self._generate_overall_reason(compatibility, overall_score)
            
            analysis["compatibility_scores"][other_id] = {
                "target_song": f"{other_song['name']} by {other_song['artist']}",
                "scores": compatibility
            }
        
        return analysis
    
    def generate_reason_codes_log(self, output_file: str = "logs.txt") -> str:
        """
        Generate comprehensive reason codes log for all songs.
        """
        log_content = []
        log_content.append("=" * 80)
        log_content.append("MUSIC MIXING SYSTEM - REASON CODES AND SCORE EXPLANATIONS")
        log_content.append("=" * 80)
        log_content.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log_content.append(f"Total Songs: {len(self.by_id)}")
        log_content.append("")
        
        # System explanation
        log_content.append("SYSTEM OVERVIEW")
        log_content.append("-" * 40)
        log_content.append("This system uses a 4-component scoring algorithm to determine song compatibility:")
        log_content.append("1. Harmonic Score (40%): Chroma vector cosine similarity")
        log_content.append("2. Tempo Score (25%): BPM difference with Gaussian weighting")
        log_content.append("3. Timbre Score (20%): MFCC and spectral feature distance")
        log_content.append("4. Energy Score (15%): Spectral centroid continuity")
        log_content.append("")
        log_content.append("Score ranges: 0.0 (poor) to 1.0 (excellent)")
        log_content.append("")
        
        # Generate analysis for each song
        for song_id in sorted(self.by_id.keys(), key=lambda x: int(x)):
            song = self.by_id[song_id]
            log_content.append("=" * 80)
            log_content.append(f"SONG ANALYSIS: {song['name']} by {song['artist']}")
            log_content.append("=" * 80)
            log_content.append(f"Song ID: {song_id}")
            log_content.append(f"Duration: {song['duration_sec']:.1f} seconds")
            log_content.append(f"Tempo: {song['tempo_bpm']:.1f} BPM")
            log_content.append("")
            
            # Get top 5 most compatible songs
            compatibilities = []
            for other_id, other_song in self.by_id.items():
                if other_id == song_id:
                    continue
                
                harmonic = self.analyze_harmonic_compatibility(song, other_song)
                tempo = self.analyze_tempo_compatibility(song, other_song)
                timbre = self.analyze_timbre_compatibility(song, other_song)
                energy = self.analyze_energy_compatibility(song, other_song)
                
                weights = {"harm": 0.40, "tempo": 0.25, "timbre": 0.20, "energy": 0.15}
                overall_score = (
                    weights["harm"] * harmonic["score"] +
                    weights["tempo"] * tempo["score"] +
                    weights["timbre"] * timbre["score"] +
                    weights["energy"] * energy["score"]
                )
                
                compatibilities.append({
                    "id": other_id,
                    "name": other_song["name"],
                    "artist": other_song["artist"],
                    "overall_score": overall_score,
                    "harmonic": harmonic,
                    "tempo": tempo,
                    "timbre": timbre,
                    "energy": energy
                })
            
            # Sort by overall score
            compatibilities.sort(key=lambda x: x["overall_score"], reverse=True)
            
            # Show top 5 most compatible songs
            log_content.append("TOP 5 MOST COMPATIBLE SONGS:")
            log_content.append("-" * 40)
            for i, comp in enumerate(compatibilities[:5], 1):
                log_content.append(f"{i}. {comp['name']} by {comp['artist']}")
                log_content.append(f"   Overall Score: {comp['overall_score']:.3f}")
                log_content.append(f"   Harmonic: {comp['harmonic']['score']:.3f} - {comp['harmonic']['reason']}")
                log_content.append(f"   Tempo: {comp['tempo']['score']:.3f} - {comp['tempo']['reason']}")
                log_content.append(f"   Timbre: {comp['timbre']['score']:.3f} - {comp['timbre']['reason']}")
                log_content.append(f"   Energy: {comp['energy']['score']:.3f} - {comp['energy']['reason']}")
                log_content.append("")
            
            # Show bottom 3 least compatible songs
            log_content.append("LEAST COMPATIBLE SONGS:")
            log_content.append("-" * 40)
            for i, comp in enumerate(compatibilities[-3:], 1):
                log_content.append(f"{i}. {comp['name']} by {comp['artist']}")
                log_content.append(f"   Overall Score: {comp['overall_score']:.3f}")
                log_content.append(f"   Harmonic: {comp['harmonic']['score']:.3f} - {comp['harmonic']['reason']}")
                log_content.append(f"   Tempo: {comp['tempo']['score']:.3f} - {comp['tempo']['reason']}")
                log_content.append(f"   Timbre: {comp['timbre']['score']:.3f} - {comp['timbre']['reason']}")
                log_content.append(f"   Energy: {comp['energy']['score']:.3f} - {comp['energy']['reason']}")
                log_content.append("")
            
            log_content.append("")
        
        # Write to file
        log_text = "\n".join(log_content)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(log_text)
        
        return output_file
    
    # Helper methods
    def _cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        """Calculate cosine similarity between two vectors."""
        na = np.linalg.norm(a)
        nb = np.linalg.norm(b)
        if na == 0 or nb == 0:
            return 0.0
        return float(np.dot(a, b) / (na * nb))
    
    def _get_harmonic_relationship(self, cos_sim: float) -> str:
        """Interpret harmonic relationship from cosine similarity."""
        if cos_sim > 0.8:
            return "Very similar harmonic content"
        elif cos_sim > 0.6:
            return "Similar harmonic characteristics"
        elif cos_sim > 0.4:
            return "Moderately different harmonics"
        elif cos_sim > 0.2:
            return "Different harmonic content"
        else:
            return "Very different harmonic content"
    
    def _get_tempo_range(self, tempo: float, ranges: Dict) -> str:
        """Get tempo range category."""
        for name, (min_tempo, max_tempo) in ranges.items():
            if min_tempo <= tempo < max_tempo:
                return name
        return "extreme"
    
    def _interpret_mfcc_mean_diff(self, diff: float) -> str:
        """Interpret MFCC mean difference."""
        if diff < 2:
            return "Very similar spectral envelope"
        elif diff < 5:
            return "Similar spectral characteristics"
        elif diff < 10:
            return "Moderately different spectral envelope"
        else:
            return "Very different spectral characteristics"
    
    def _interpret_mfcc_std_diff(self, diff: float) -> str:
        """Interpret MFCC standard deviation difference."""
        if diff < 1:
            return "Similar spectral variability"
        elif diff < 3:
            return "Moderately different spectral variability"
        else:
            return "Very different spectral variability"
    
    def _interpret_centroid_diff(self, diff: float) -> str:
        """Interpret spectral centroid difference."""
        if diff < 200:
            return "Similar brightness"
        elif diff < 500:
            return "Moderately different brightness"
        else:
            return "Very different brightness"
    
    def _categorize_energy(self, energy: float) -> str:
        """Categorize energy level."""
        if energy < 1000:
            return "Very low energy"
        elif energy < 1500:
            return "Low energy"
        elif energy < 2500:
            return "Medium energy"
        elif energy < 3500:
            return "High energy"
        else:
            return "Very high energy"
    
    def _generate_overall_reason(self, compatibility: Dict, overall_score: float) -> str:
        """Generate overall reason for compatibility."""
        if overall_score > 0.8:
            return "Excellent overall compatibility - ideal for mixing"
        elif overall_score > 0.6:
            return "Good compatibility - suitable for mixing"
        elif overall_score > 0.4:
            return "Moderate compatibility - may work with careful mixing"
        else:
            return "Poor compatibility - not recommended for mixing"


def main():
    """Main function to generate reason codes."""
    print("Generating reason codes and score explanations...")
    
    try:
        generator = ReasonCodesGenerator()
        output_file = generator.generate_reason_codes_log()
        print(f"Reason codes generated successfully: {output_file}")
        print(f"Total songs analyzed: {len(generator.by_id)}")
        
    except Exception as e:
        print(f"Error generating reason codes: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
