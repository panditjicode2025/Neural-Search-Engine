import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/search"

st.title("Neural Search Engine")

query = st.text_input("Enter search query")

top_k = st.slider("Number of results", 1, 10, 5)

if st.button("Search"):

    response = requests.post(
        API_URL,
        json={"text": query, "top_k": top_k}
    )

    results = response.json()["results"]

    for r in results:

        st.subheader(f"Result {r['rank']}")
        st.write(r["text"])
        st.write(f"Score: {r['score']}")
        st.markdown("---")