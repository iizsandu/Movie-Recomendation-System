import streamlit as st
import pickle

movies_df = pickle.load(open('movies.pkl','rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recomendation System')


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list1:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies




import streamlit as st

selected_movie = st.selectbox(
    'Select a Movie from the dropdown',
    movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)