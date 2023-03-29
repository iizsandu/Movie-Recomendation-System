import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title('Movie Recomedation System')

movies_df = pickle.load(open('movies.pkl','rb'))
movies_list = movies_df['title'].values

cv = CountVectorizer(max_features=5000,stop_words = 'english')
vectors = cv.fit_transform(movies_df['tags']).toarray()
similarity = cosine_similarity(vectors)

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