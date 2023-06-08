import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")
#load ./src/introduction.md and display as markdown
with open("./src/introduction.md","r") as f:
    introduction = f.read()
st.markdown(introduction)
