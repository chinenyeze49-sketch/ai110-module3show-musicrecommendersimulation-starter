from src.recommender import load_songs, recommend_songs

def print_table(recommendations):
    print(f"\n{'Rank':<5} {'Title':<25} {'Score':<8} {'Reasons'}")
    print("-" * 70)
    for i, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"{i:<5} {song['title']:<25} {score:<8.2f} {explanation}")

def main() -> None:
    songs = load_songs("data/songs.csv")
    profiles = [
        ("High-Energy Pop (Genre-First)", {"genre": "pop", "mood": "happy", "energy": 0.9, "mode": "genre-first", "mood_tag": "euphoric", "decade": 2020}),
        ("Chill Lofi (Mood-First)", {"genre": "lofi", "mood": "chill", "energy": 0.3, "mode": "mood-first", "mood_tag": "nostalgic", "decade": 2020}),
        ("Deep Intense Rock (Energy-Focused)", {"genre": "rock", "mood": "intense", "energy": 0.95, "mode": "energy-focused", "mood_tag": "aggressive", "decade": 2010}),
    ]
    for profile_name, user_prefs in profiles:
        print(f"\n{'='*70}")
        print(f"Profile: {profile_name}")
        print(f"{'='*70}")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_table(recommendations)

if __name__ == "__main__":
    main()
