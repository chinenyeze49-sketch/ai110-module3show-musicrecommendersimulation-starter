from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv

@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def score_song(self, user: UserProfile, song: Song) -> float:
        score = 0.0
        if song.genre == user.favorite_genre:
            score += 2.0
        if song.mood == user.favorite_mood:
            score += 2.0
        score += 1 - abs(song.energy - user.target_energy)
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = sorted(self.songs, key=lambda s: self.score_song(user, s), reverse=True)
        return scored[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"matches your favorite genre ({song.genre})")
        if song.mood == user.favorite_mood:
            reasons.append(f"matches your preferred mood ({song.mood})")
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.2:
            reasons.append("has similar energy to your preference")
        return "Recommended because it " + ", and ".join(reasons) if reasons else "General recommendation"

def load_songs(csv_path: str) -> List[Dict]:
    songs = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> float:
    score = 0.0
    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
    if song["mood"] == user_prefs.get("mood"):
        score += 2.0
    score += 1 - abs(song["energy"] - user_prefs.get("energy", 0.5))
    return score

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored = []
    for song in songs:
        s = score_song(user_prefs, song)
        reasons = []
        if song["genre"] == user_prefs.get("genre"):
            reasons.append(f"matches your favorite genre ({song['genre']})")
        if song["mood"] == user_prefs.get("mood"):
            reasons.append(f"matches your preferred mood ({song['mood']})")
        if abs(song["energy"] - user_prefs.get("energy", 0.5)) < 0.2:
            reasons.append("has similar energy to your preference")
        explanation = "Recommended because it " + ", and ".join(reasons) if reasons else "General recommendation"
        scored.append((song, s, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]