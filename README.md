# 🎵 Music Recommendation System

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge&logo=supabase">
<img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn">
</p>

---

# 📖 Project Overview

The **Music Recommendation System** is an intelligent web application that recommends songs to users based on their selected mood, genre, artist preferences, and listening patterns. The application aims to provide personalized music suggestions through a user-friendly interface and recommendation algorithms.

The system is built using **Python**, **Flask**, **HTML**, **CSS**, **JavaScript**, and **Supabase (PostgreSQL)** for storing user and music data.

---

# 🎯 Objectives

- Recommend songs based on user preferences.
- Provide personalized music suggestions.
- Create an easy-to-use music browsing interface.
- Improve user experience through intelligent recommendations.
- Maintain user profiles and recommendation history.

---

# ✨ Features

## 🎧 User Features

- User Registration
- Secure Login
- Browse Music Library
- Search Songs
- Filter by Genre
- Filter by Artist
- Mood-Based Music Recommendation
- Personalized Recommendations
- Recently Played Songs
- Favorite Songs
- Playlist Management
- User Profile Management

---

## 🎵 Music Features

- Song Catalog
- Artist Details
- Album Information
- Genre Classification
- Song Duration
- Song Ratings
- Trending Songs
- Recommended Songs

---

## 🤖 Recommendation Engine

- Mood-Based Recommendation
- Genre-Based Recommendation
- Artist-Based Recommendation
- Similar Song Recommendation
- Personalized Suggestions
- Smart Filtering
- Recommendation History

---

## 📊 Dashboard

- Total Songs
- Total Artists
- Total Genres
- User Activity
- Recommendation Statistics
- Recently Added Songs

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
      HTML • CSS • JavaScript
                  │
                  ▼
            Flask Application
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 Recommendation Engine   Supabase Database
```

---

# 🛠️ Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

## Backend

- Python
- Flask

## Database

- Supabase
- PostgreSQL

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# 📂 Project Structure

```
Music-Recommendation-System/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── recommendations.html
│   ├── profile.html
│
├── models/
├── routes/
├── database/
├── recommendation/
├── app.py
├── requirements.txt
├── config.py
└── README.md
```

---

# 📋 Modules

## 🔐 Authentication Module

- User Registration
- User Login
- Logout
- Session Management
- Password Encryption

---

## 👤 User Module

- Profile Management
- Favorite Songs
- Listening History
- Recently Played

---

## 🎵 Music Module

- Browse Songs
- Search Songs
- Genre Filtering
- Artist Filtering
- Song Details

---

## 🤖 Recommendation Module

- Mood Analysis
- Similar Song Detection
- Personalized Recommendation
- Recommendation History

---

## ❤️ Playlist Module

- Create Playlist
- Add Songs
- Remove Songs
- Favorite Songs

---

# 🗄️ Database Schema

The system uses **Supabase PostgreSQL**.

## Main Tables

### users

| Field | Type |
|-------|------|
| id | UUID |
| username | VARCHAR |
| email | VARCHAR |
| password | TEXT |

---

### songs

| Field | Type |
|-------|------|
| id | UUID |
| title | VARCHAR |
| artist | VARCHAR |
| album | VARCHAR |
| genre | VARCHAR |
| mood | VARCHAR |
| duration | INTEGER |

---

### playlists

| Field | Type |
|-------|------|
| playlist_id | UUID |
| user_id | UUID |
| playlist_name | VARCHAR |

---

### playlist_songs

| Field | Type |
|-------|------|
| id | UUID |
| playlist_id | UUID |
| song_id | UUID |

---

### recommendations

| Field | Type |
|-------|------|
| id | UUID |
| user_id | UUID |
| song_id | UUID |
| recommended_at | TIMESTAMP |

---

### favorites

| Field | Type |
|-------|------|
| id | UUID |
| user_id | UUID |
| song_id | UUID |

---

# 🔄 Workflow

```
User Login
      │
      ▼
Browse Music
      │
      ▼
Select Mood / Genre / Artist
      │
      ▼
Recommendation Engine
      │
      ▼
Generate Personalized Songs
      │
      ▼
Display Recommended Songs
      │
      ▼
Save Recommendation History
```

---

# 🔒 Security Features

- Password Hashing
- Secure Login
- Session Management
- User Authentication
- Protected Routes
- Secure Database Access

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Varshitha272004/Music-Recommendation-System.git
```

---

## Navigate to Project

```bash
cd Music-Recommendation-System
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

SECRET_KEY=your_secret_key
```

---

## Run Application

```bash
python app.py
```

Open the browser:

```
http://127.0.0.1:5000

---

# 🚀 Future Enhancements

- AI-Based Music Recommendation
- Emotion Detection Using Facial Expressions
- Voice Search
- Lyrics Search
- Recently Trending Songs
- Mobile Application
- Dark Mode
- Multi-Language Support
- Admin Dashboard
- Cloud Deployment

--

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

## 📧 Contact

For suggestions or improvements, feel free to open an issue or connect through GitHub.

Happy Coding! 🎵🚀
