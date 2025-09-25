# mix_algo.py
from __future__ import annotations
import math, numpy as np, pandas as pd
from typing import Callable, Dict, List, Optional, Tuple

class MixAlgo:
    """
    Smooth, natural auto-mix selector.
    - Music-first shortlist (harmony -> tempo -> timbre -> energy)
    - Text (qwen_analysis) tie-break among top-K
    - Short crossfade (default 4 beats), after-release feel approximation
    - Always computes next-two queue

    Expected df columns (per track):
      id, name, artist, qwen_analysis,
      tempo_bpm, mfcc_mean, mfcc_std, centroid_mean,
      first_slice_centroid_mean, last_slice_centroid_mean,
      first_chroma_vec_12, last_chroma_vec_12, duration_sec
    """

    def __init__(
        self,
        weights: Dict[str, float] = None,      # music scoring weights
        bpm_tol: float = 6.0,                  # tempo gaussian tol (BPM)
        max_warp: float = 0.12,                # ±12% max warp
        k_shortlist: int = 5,                  # top-K by music before text
        crossfade_beats: int = 4               # short crossfade
    ):
        self.W = weights or dict(harm=0.40, tempo=0.25, timbre=0.20, energy=0.15)
        self.bpm_tol = bpm_tol
        self.max_warp = max_warp
        self.k_shortlist = k_shortlist
        self.crossfade_beats = crossfade_beats

        self.df: Optional[pd.DataFrame] = None
        self.by_id: Dict[str, pd.Series] = {}
        self.embed: Dict[str, np.ndarray] = {}
        self.energy_scale: float = 1.0  # for energy continuity normalization
        
        # Song history tracking
        self.played_songs: List[str] = []  # List of song IDs that have been played
        self.max_history: int = 50  # Maximum songs to remember (prevents infinite memory)

    # ---------- public API ----------

    def fit(
        self,
        df: pd.DataFrame,
        embedding_func: Optional[Callable[[str], np.ndarray]] = None,
        embeddings: Optional[Dict[str, np.ndarray]] = None
    ) -> "MixAlgo":
        """Prepare data and text embeddings (either provide dict, or a function)."""
        self.df = df.copy()
        # Make sure chroma vectors are arrays (parse JSON strings from CSV)
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

        # Build id index
        self.by_id = {str(r["id"]): r for _, r in self.df.iterrows()}

        # Energy scale for continuity (robust)
        if "centroid_mean" in self.df.columns:
            vals = self.df["centroid_mean"].dropna().to_numpy()
            if len(vals) >= 5:
                mad = np.median(np.abs(vals - np.median(vals))) + 1e-9
                self.energy_scale = 6 * mad  # wider than 3σ, keeps gentle penalties
            else:
                self.energy_scale = max(1.0, np.std(vals) + 1e-9)

        # Embeddings
        self.embed = {}
        if embeddings:
            # Use provided dict {id: vector}
            for tid, vec in embeddings.items():
                self.embed[str(tid)] = self._as_vec(vec)
        elif embedding_func:
            # Compute from qwen_analysis
            for tid, row in self.by_id.items():
                text = row.get("qwen_analysis", "")
                self.embed[tid] = self._as_vec(embedding_func(text)) if isinstance(text, str) else None
        # else: no text tie-break if no embeddings

        return self

    def next_two(self, current_id: str) -> Tuple[Optional[str], Optional[str], Dict]:
        """Return (next_id, next_next_id, debug_info)."""
        nxt, info1 = self._pick_next(current_id)
        nxt2, info2 = (None, {}) if nxt is None else self._pick_next(nxt)
        return nxt, nxt2, {"first": info1, "second": info2}
    
    def mark_song_played(self, song_id: str) -> None:
        """Mark a song as played to avoid repetition."""
        song_id = str(song_id)
        if song_id not in self.played_songs:
            self.played_songs.append(song_id)
            # Keep only the most recent songs to prevent infinite memory
            if len(self.played_songs) > self.max_history:
                self.played_songs = self.played_songs[-self.max_history:]
    
    def reset_history(self) -> None:
        """Reset the played songs history."""
        self.played_songs = []
    
    def get_available_songs(self) -> List[str]:
        """Get list of song IDs that haven't been played recently."""
        all_songs = set(self.by_id.keys())
        played_songs = set(self.played_songs)
        return list(all_songs - played_songs)
    
    def generate_playlist(self, start_song_id: str, length: int = 10) -> List[Dict]:
        """
        Generate a complete playlist with automatic history management.
        Returns list of song dictionaries with metadata.
        """
        playlist = []
        current_id = str(start_song_id)
        
        # Mark starting song as played
        self.mark_song_played(current_id)
        
        for i in range(length):
            # Get next song
            next_id, debug_info = self._pick_next(current_id)
            
            if next_id is None:
                # This should never happen with our fallback logic
                break
                
            # Get song info
            song_info = self.by_id[next_id]
            playlist.append({
                'position': i + 1,
                'song_id': next_id,
                'name': song_info['name'],
                'artist': song_info['artist'],
                'tempo_bpm': song_info['tempo_bpm'],
                'duration_sec': song_info['duration_sec'],
                'debug_info': debug_info
            })
            
            # Mark as played and move to next
            self.mark_song_played(next_id)
            current_id = next_id
        
        return playlist

    # ---------- core selection ----------

    def _pick_next(self, current_id: str) -> Tuple[Optional[str], Dict]:
        A = self.by_id.get(str(current_id))
        if A is None:
            return None, {"reason": f"id {current_id} not found"}

        # Get available songs (not recently played)
        available_songs = self.get_available_songs()
        
        # If no songs available, reset history and try again
        if not available_songs:
            self.reset_history()
            available_songs = self.get_available_songs()
            if not available_songs:
                return None, {"reason": "no songs available in dataset"}

        # Candidate prefilter by tempo (only from available songs)
        cand_rows = []
        for tid in available_songs:
            if tid == str(current_id):
                continue
            B = self.by_id[tid]
            if self._tempo_prefilter(A, B):
                cand_rows.append(B)
        
        # If no tempo-compatible songs, relax tempo filter and use all available
        if not cand_rows:
            for tid in available_songs:
                if tid == str(current_id):
                    continue
                B = self.by_id[tid]
                cand_rows.append(B)

        # If still no candidates, fail explicitly - no good matches available
        if not cand_rows:
            raise ValueError(f"No suitable songs found for mixing after current song {current_id}. Available songs: {len(available_songs)}")

        # Music score
        scored = []
        for B in cand_rows:
            s = self._music_score(A, B)
            scored.append((str(B["id"]), s))
        scored.sort(key=lambda x: x[1], reverse=True)

        # Shortlist
        shortlist = scored[: self.k_shortlist]

        # Text tie-break among shortlist
        chosen_id = self._tie_break_text(str(A["id"]), shortlist)

        # Cut plan
        cut = self._compute_cut(self.by_id[str(chosen_id)], A)

        # Debug
        info = {
            "shortlist": shortlist,
            "chosen": chosen_id,
            "cut": cut,
            "available_songs": len(available_songs),
            "played_songs": len(self.played_songs)
        }
        return chosen_id, info

    # ---------- scoring pieces ----------

    def _tempo_prefilter(self, A: pd.Series, B: pd.Series) -> bool:
        a, b = float(A["tempo_bpm"]), float(B["tempo_bpm"])
        d = abs(a - b)
        rel = d / max(a, b, 1e-6)
        return (d <= 8.0) or (rel <= self.max_warp)

    def _music_score(self, A: pd.Series, B: pd.Series) -> float:
        harm = self._harm_score(A, B)            # [0..1]
        tempo = self._tempo_score(A, B)          # [0..1]
        timbre = self._timbre_score(A, B)        # [0..1]
        energy = self._energy_score(A, B)        # [0..1]
        W = self.W
        return (W["harm"]*harm + W["tempo"]*tempo +
                W["timbre"]*timbre + W["energy"]*energy)

    def _harm_score(self, A: pd.Series, B: pd.Series) -> float:
        a = A.get("last_chroma_vec_12", None)
        b = B.get("first_chroma_vec_12", None)
        if not (isinstance(a, np.ndarray) and isinstance(b, np.ndarray)):
            raise ValueError(f"Missing chroma vectors for harmonic analysis. Song A: {A.get('id', 'unknown')}, Song B: {B.get('id', 'unknown')}")
        return self._cos(a, b)  # already in [0..1] by _cos()

    def _tempo_score(self, A: pd.Series, B: pd.Series) -> float:
        a, b = float(A["tempo_bpm"]), float(B["tempo_bpm"])
        d = abs(a - b)
        base = math.exp(- (d / self.bpm_tol) ** 2)
        rel = d / max(a, b, 1e-6)
        return base if rel <= self.max_warp else 0.5 * base

    def _timbre_score(self, A: pd.Series, B: pd.Series) -> float:
        vecA = np.array([float(A["mfcc_mean"]), float(A["mfcc_std"]), float(A["centroid_mean"])], float)
        vecB = np.array([float(B["mfcc_mean"]), float(B["mfcc_std"]), float(B["centroid_mean"])], float)
        d = np.linalg.norm(vecA - vecB)
        return float(1.0 / (1.0 + d))  # smaller distance → closer to 1

    def _energy_score(self, A: pd.Series, B: pd.Series) -> float:
        a = float(A.get("last_slice_centroid_mean", A.get("centroid_mean", 0.0)))
        b = float(B.get("first_slice_centroid_mean", B.get("centroid_mean", 0.0)))
        s = self.energy_scale or 1.0
        return 1 - min(1.0, abs(a - b) / s)

    # ---------- text tie-break ----------

    def _tie_break_text(self, aid: str, shortlist: List[Tuple[str, float]]) -> str:
        # If no text embeddings available, return the top music-scored song
        if not self.embed or self.embed.get(aid) is None:
            return shortlist[0][0]  # Return highest music score

        a_vec = self.embed.get(aid)
        best_id, best_sim = shortlist[0][0], -1.0
        for tid, _ in shortlist:
            b_vec = self.embed.get(tid)
            if b_vec is None:
                # If any candidate lacks embedding, fall back to music score
                return shortlist[0][0]
            sim = self._cos_raw(a_vec, b_vec)  # [-1..1]
            if sim > best_sim:
                best_id, best_sim = tid, sim
        return best_id

    # ---------- cut planning ----------

    def _compute_cut(self, B: pd.Series, A: pd.Series) -> Dict:
        """
        Short crossfade after release feel:
        - Crossfade length = crossfade_beats at A's tempo.
        - Align B's intro to A's outro; lightly time-stretch B's intro if needed.
        - Return times in seconds (approx; for precise, compute beats from audio at runtime).
        """
        a_bpm = float(A["tempo_bpm"]); b_bpm = float(B["tempo_bpm"])
        beat_dur = 60.0 / max(a_bpm, 1e-6)
        crossfade_sec = self.crossfade_beats * beat_dur

        # Place cut: end of A minus crossfade; B in at 0
        A_dur = float(A.get("duration_sec", crossfade_sec*2))
        A_out = max(0.0, A_dur - crossfade_sec)
        B_in = 0.0

        # Stretch B intro to align beats (limited by max_warp)
        stretch_ratio = np.clip(a_bpm / max(b_bpm, 1e-6), 1 - self.max_warp, 1 + self.max_warp)

        return dict(
            crossfade_sec=float(crossfade_sec),
            A_out_time_sec=float(A_out),
            B_in_time_sec=float(B_in),
            stretch_ratio=float(stretch_ratio),
            target_bpm_for_B=float(a_bpm)  # during the crossfade
        )

    # ---------- math helpers ----------

    @staticmethod
    def _as_vec(x) -> Optional[np.ndarray]:
        if x is None: return None
        v = np.asarray(x, float)
        return v if v.ndim == 1 else v.reshape(-1)

    @staticmethod
    def _cos_raw(a: np.ndarray, b: np.ndarray) -> float:
        na = np.linalg.norm(a); nb = np.linalg.norm(b)
        if na == 0 or nb == 0: return 0.0
        return float(np.dot(a, b) / (na * nb))

    def _cos(self, a: np.ndarray, b: np.ndarray) -> float:
        """Return cosine similarity mapped to [0,1]."""
        return 0.5 * (1.0 + self._cos_raw(a, b))
