import streamlit as st

def menu():
  st.set_page_config(page_title="Breathflow", page_icon='🕊️')
  st.sidebar.page_link("app.py", label="💪 Exercise Recommender")
  st.sidebar.page_link("pages/feedback.py", label="🖼️ Posture Analysis")
  st.sidebar.page_link("pages/grading.py", label="📺 Video Analysis")
