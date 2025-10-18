import langchain_helper as lch
import streamlit as st

st.title("LangChain Tutorial")

person_type = st.sidebar.selectbox(
    "human type", ("happy person", "sad person")
)

hair_color = st.sidebar.selectbox(
    "color", ("red", "yellow")
)
if hair_color:
    gender = st.sidebar.selectbox(
        "gender", ("male", "female")
    )

if gender == 'male':
    text_area = st.sidebar.text_area(
        label="Comment",
        max_chars=10
    )

if st.button("Generate name"):
    response = st.write(lch.generate_name(person_type, hair_color, gender))
    st.text(response)