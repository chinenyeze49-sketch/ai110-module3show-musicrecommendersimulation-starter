# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name
**VibeFinder 1.0**

## 2. Goal / Task
This recommender suggests songs from a small catalog based on a user's 
preferred genre, mood, and energy level.

## 3. Data Used
- 10 songs in the catalog
- Features: genre, mood, energy, tempo_bpm, valence, danceability, acousticness
- Genres: pop, lofi, rock, jazz, synthwave, ambient, indie pop
- Limit: very small dataset, missing many genres like hip-hop, R&B, country

## 4. Algorithm Summary
Each song gets a score. Genre match adds 2 points. Mood match adds 1 point. 
Energy similarity adds up to 1 point. Top 5 are recommended.

## 5. Observed Behavior / Biases
Biased toward pop and lofi users. Rock profile only matched one song by genre.

## 6. Evaluation Process
Tested three profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock.
Also tested changing genre weight from 2.0 to 1.0.

## 7. Intended Use and Non-Intended Use
Intended: Classroom exploration only.
Not Intended: Real music recommendations for actual users.

## 8. Ideas for Improvement
- Add more diverse songs
- Include tempo and danceability in scoring
- Support multiple user profiles

## 9. Personal Reflection
My biggest learning was that dataset balance matters as much as scoring logic.
Simple algorithms can still feel surprisingly accurate for well-represented genres.
