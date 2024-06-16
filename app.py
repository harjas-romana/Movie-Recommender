# import pickle
# import streamlit as st
# import requests
# import time

# def fetch_poster(movie_id):
#     api_key = 'c9bd7d6f35fb8240a8bf7ffa6cc24c1b'
#     url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)

#     max_retries = 3
#     retry_delay = 1  # seconds

#     for attempt in range(max_retries):
#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
#             data = response.json()
#             poster_path = data['poster_path']
#             full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#             return full_path
#         except requests.exceptions.RequestException as e:
#             if attempt < max_retries - 1:
#                 print(f"Request error on attempt {attempt+1}. Retrying in {retry_delay} seconds...")
#                 time.sleep(retry_delay)
#             else:
#                 print(f"Failed to retrieve poster for movie {movie_id}: {e}")
#                 return None

# def recommend(movie):
#     '''Function takes a movie (string) and returns 6 similar movie names list and 6 movie poster list'''
#     index = movies[movies['title'] == movie].index[0]
#     top_20 = similarity[index]
    
#     recommended_movie_names = []
#     recommended_movie_posters = []
    
#     for i in top_20[1:7]:
        
#         movie_id = movies.iloc[i].movie_id
#         # fetch the movie poster
#         poster = fetch_poster(movie_id)
        
#         recommended_movie_posters.append(poster)
#         recommended_movie_names.append(movies.iloc[i].title)

#     return recommended_movie_names, recommended_movie_posters

# st.header('Movie Recommender System')
# movies = pickle.load(open('movie_list.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))

# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )

# if st.button('Show Recommendation'):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
        
#     col4, col5, col6 = st.columns(3)
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
#     with col6:
#         st.text(recommended_movie_names[5])
#         st.image(recommended_movie_posters[5])


import pickle
import streamlit as st
import requests
import time
import os
# Set the environment variable for Netlify
os.environ['NETLIFY'] = 'true'

def fetch_poster(movie_id):
    api_key = 'c9bd7d6f35fb8240a8bf7ffa6cc24c1b'
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)

    max_retries = 3
    retry_delay = 1  # seconds

    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                print(f"Request error on attempt {attempt+1}. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"Failed to retrieve poster for movie {movie_id}: {e}")
                return None

def recommend(movie):
    '''Function takes a movie (string) and returns 6 similar movie names list'''
    index = movies[movies['title'] == movie].index[0]
    top_20 = similarity[index]
    
    recommended_movie_names = []
    
    for i in top_20[1:7]:
        recommended_movie_names.append(movies.iloc[i].title)

    return recommended_movie_names

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    st.write("Recommended Movies:")
    for movie in recommended_movie_names:
        st.write(movie)