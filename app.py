import pandas as pd
import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e5f8c4370e5bf80a5582eaf0c2232534&language=en=US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

# Load the movie dictionary from a pickle file

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

# Create a DataFrame from the movie dictionary
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Streamlit app title
st.title('Movie Recommendation System')

# Selectbox to choose a movie
option = st.selectbox('Which movie?', movies['title'].values)

# Display the selected movie
if st.button('Recommend'):
    names,posters = recommend(option)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

# You c an add more functionality here, such as displaying recommendations based on the selected movie.
# For example, if you have a function get_recommendations(movie_title), you can call it like this:
# recommendations = get_recommendations(option)
# st.write('Recommendations:', recommendations)
