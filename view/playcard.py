import requests
import streamlit as st
from datetime import timedelta


class Playcard(object):

    @st.cache_data(ttl=timedelta(minutes=30))
    def playcard(language: str = "en-US"):
        r = requests.get("https://valorant-api.com/v1/playercards", params={'language': language})
        return r.json() if r.ok else None
