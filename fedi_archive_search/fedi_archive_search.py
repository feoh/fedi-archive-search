import streamlit as st

st.title("Fediverse Archive Searcher")

from_date = st.date_input("From date")
to_date = st.date_input("To date")

search_term = st.text_input("Search term")
