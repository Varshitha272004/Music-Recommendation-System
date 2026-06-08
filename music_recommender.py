import streamlit as st
import pandas as pd
import numpy as np
import time
from collections import defaultdict
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# --- Page Setup ---
st.set_page_config(page_title="Music Recommender", layout="wide")
st.title("🎵 Music Recommendation System")

# --- Load CSV Files from Local Folder ---
try:
    data = pd.read_csv("data.csv")
    genre_data = pd.read_csv("data_by_genres.csv")
    year_data = pd.read_csv("data_by_year.csv")
except FileNotFoundError:
    st.error("One or more CSV files (data.csv, data_by_genres.csv, data_by_year.csv) are missing in the project folder.")
    st.stop()

number_cols = data.select_dtypes(np.number).columns.tolist()

# --- Clustering ---
song_cluster_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('kmeans', KMeans(n_clusters=20, verbose=False))
])
X = data[number_cols]
song_cluster_pipeline.fit(X)
data['cluster_label'] = song_cluster_pipeline.predict(X)

# --- Spotify Setup (Hardcoded credentials) ---
client_id = "daebbd81d1e84fa7b83757614cfb16f9"
client_secret = "ddc6deb241974cc29177b4cc381bb3fd"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
), requests_timeout=(10, 30))

# --- Helper Functions ---
def find_song(name, year, retries=3, delay=2):
    for attempt in range(retries):
        try:
            results = sp.search(q=f'track: {name} year: {year}', limit=1)
            if results['tracks']['items']:
                return results['tracks']['items'][0]
            return None
        except Exception:
            time.sleep(delay)
    return None

def get_song_data(song, spotify_data):
    filtered = spotify_data[(spotify_data['name'] == song['name']) & (spotify_data['year'] == song['year'])]
    if not filtered.empty:
        return filtered.iloc[0]
    
    found_song = find_song(song['name'], song['year'])
    if found_song is None:
        return None
    
    filtered = spotify_data[spotify_data['name'].str.contains(found_song['name'], case=False, na=False)]
    if not filtered.empty:
        return filtered.iloc[0]

    return None

def get_mean_vector(song_list, spotify_data):
    song_vectors = []
    for song in song_list:
        song_data = get_song_data(song, spotify_data)
        if song_data is None:
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)

    if not song_vectors:
        return None
    return np.mean(np.array(song_vectors), axis=0)

def flatten_dict_list(dict_list):
    flat = defaultdict(list)
    for key in dict_list[0].keys():
        for d in dict_list:
            flat[key].append(d[key])
    return flat

def recommend_songs(song_list, spotify_data, n_songs=10):
    song_dict = flatten_dict_list(song_list)
    song_center = get_mean_vector(song_list, spotify_data)
    if song_center is None:
        return pd.DataFrame()

    scaler = song_cluster_pipeline.named_steps['scaler']
    scaled_data = scaler.transform(spotify_data[number_cols])
    scaled_center = scaler.transform(song_center.reshape(1, -1))

    distances = cdist(scaled_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])
    rec_songs = spotify_data.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]

    return rec_songs[['name', 'year', 'artists']]

# --- UI Inputs ---
st.subheader("🎧 Enter a song to get recommendations")
song_name = st.text_input("Song Name", value="Blinding Lights")
song_year = st.number_input("Year", min_value=1900, max_value=2025, value=2020)

if st.button("Recommend"):
    song_input = [{'name': song_name, 'year': int(song_year)}]
    recs = recommend_songs(song_input, data)
    if not recs.empty:
        st.success("Here are your recommendations:")
        st.dataframe(recs)
    else:
        st.warning("Sorry, couldn't find suitable recommendations.")
