# 🎵 Music Recommendation System

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge&logo=supabase">
<img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn">
</p>

---

# 🎵 Mood-Based Music Recommendation System

A smart Music Recommendation System that suggests songs based on the user's selected mood. The application uses Machine Learning techniques to provide personalized music recommendations through an interactive **Streamlit** interface while securely managing data using **Supabase**.

---

## 📖 Overview

The Mood-Based Music Recommendation System is an AI-powered web application that helps users discover music that matches their current mood. Instead of manually searching through thousands of songs, users can simply choose a mood, and the system generates personalized song recommendations.

The application provides a clean and interactive interface using Streamlit and leverages Machine Learning algorithms for intelligent recommendations.

---

## ✨ Features

- 🎭 Mood-Based Music Recommendations
- 🎵 Personalized Song Suggestions
- 🔍 Search Songs by Title
- 🎼 Browse Songs by Genre
- 🎤 Artist-Based Recommendations
- ❤️ Favorite Songs Management
- 📋 Recommendation History
- 👤 User Authentication
- 📊 Interactive Dashboard
- ⚡ Fast Recommendation Engine
- ☁️ Cloud Deployment using Streamlit
- 🔒 Secure User Authentication with Supabase

---

## 🛠️ Technology Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- Supabase (PostgreSQL)

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Development Tools
- Visual Studio Code
- Git
- GitHub

### Deployment
- Streamlit Community Cloud

---

## 🏗️ System Architecture

```
                User
                  │
                  ▼
        Streamlit Web Interface
                  │
                  ▼
      Music Recommendation Engine
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 Machine Learning      Supabase Database
     Model             (PostgreSQL)
```

---

## 📂 Project Structure

```
Music-Recommendation-System/
│
├── assets/
├── data/
├── models/
├── utils/
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## 📋 Modules

### 🔐 Authentication Module

- User Registration
- User Login
- Secure Authentication
- Session Management

---

### 🎵 Music Recommendation Module

- Mood-Based Recommendation
- Genre-Based Recommendation
- Artist-Based Recommendation
- Similar Song Recommendation

---

### 👤 User Module

- User Profile
- Favorite Songs
- Recommendation History

---

### 📊 Dashboard Module

- User Activity
- Recently Recommended Songs
- Music Statistics

---

## 🗄️ Database Schema

The application uses **Supabase PostgreSQL** as the backend database.

### Users

| Field | Type |
|------|------|
| id | UUID |
| username | VARCHAR |
| email | VARCHAR |
| password | TEXT |

---

### Songs

| Field | Type |
|------|------|
| song_id | UUID |
| title | VARCHAR |
| artist | VARCHAR |
| album | VARCHAR |
| genre | VARCHAR |
| mood | VARCHAR |
| duration | INTEGER |

---

### Recommendations

| Field | Type |
|------|------|
| recommendation_id | UUID |
| user_id | UUID |
| song_id | UUID |
| recommended_at | TIMESTAMP |

---

### Favorites

| Field | Type |
|------|------|
| favorite_id | UUID |
| user_id | UUID |
| song_id | UUID |

---

## 🔄 Workflow

```
User Login
      │
      ▼
Select Mood
      │
      ▼
Recommendation Engine
      │
      ▼
Machine Learning Model
      │
      ▼
Recommended Songs
      │
      ▼
Display Results
      │
      ▼
Save Recommendation History
```

---

## 🔒 Security Features

- Secure User Authentication
- Session Management
- Encrypted Password Storage
- Protected User Data
- Secure Database Access

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Varshitha272004/Music-Recommendation-System.git
```

### Navigate to the Project Folder

```bash
cd Music-Recommendation-System
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and add:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

### Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 🌐 Live Demo

🚀 **Live Application**

> Add your deployed Streamlit application link here.

Example:

```
https://your-app-name.streamlit.app
```

---

## 📸 Screenshots

Add screenshots of:

- Login Page
- Home Page
- Mood Selection
- Music Recommendations
- Search Songs
- User Dashboard

---

## 🚀 Future Enhancements

- AI-Based Personalized Recommendations
- Lyrics Search
- Voice-Based Music Search
- Emotion Detection using Facial Expressions
- Playlist Generation
- Recently Played Songs
- Music Popularity Analytics
- Multi-Language Support
- Mobile Application
- Admin Dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Create a Pull Request.

---

## 📜 License

This project is developed for educational and learning purposes.

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. Your support is appreciated!
