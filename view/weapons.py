import requests
import streamlit as st
from datetime import timedelta


class Weapons(object):

    @st.cache_data(ttl=timedelta(minutes=30))
    def weapons(language: str = "en-US"):
        r = requests.get("https://valorant-api.com/v1/weapons", params={'language': language})
        return r.json() if r.ok else None
