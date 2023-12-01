import streamlit as st
import youtube_helper as yth
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="Enter the YouTube Url:",
            max_chars=50
        )
        query = st.sidebar.text_area(
            label="Ask me about the video: ",
            max_chars=50,
            key="query"
        )

        submit_button = st.form_submit_button(label="Submit")

if query and youtube_url:
    db = yth.create_vector_db_from_youtube_Url(youtube_url)
    response = yth.get_response_from_query(db, query)
    st.subheader("Answer")
    st.text(textwrap.fill(response, width=80))