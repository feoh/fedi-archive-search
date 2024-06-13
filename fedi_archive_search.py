import streamlit as st
import duckdb

st.title("Fediverse Archive Searcher")


from_date = st.date_input("From date")
to_date = st.date_input("To date")

search_term = st.text_input("Search term")

statuses=duckdb.sql("select statuses FROM read_json_auto('oldbytes.space.user.feoh.json', maximum_object_size=160000000)")


st.write(statuses)
