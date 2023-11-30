import langchain_helper as lch
import streamlit as st

st.title("Pets Name generator")

user_animal_type = st.sidebar.selectbox("What is your Pet?",("Cat", "Dog","Cow"))

if user_animal_type == "Cat":
    user_pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)
if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area(label="What color is your Dog?", max_chars=15)
if user_animal_type == "Cow":
    user_pet_color = st.sidebar.text_area(label="What color is your Cow?", max_chars=15)

if user_pet_color:
    response = lch.generate_pet_name(user_animal_type,user_pet_color)
    st.text(response['pet_name'])