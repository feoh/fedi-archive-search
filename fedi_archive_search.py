import streamlit as st
import duckdb

st.title("Fediverse Archive Searcher")


from_date = st.date_input("From date")
to_date = st.date_input("To date")

search_term = st.text_input("Search term")

j = duckdb.read_json('oldbytes.space.user.feoh.json', maximum_object_size=640000000);


statuses = duckdb.sql("select statuses from j")
print(statuses)
