import streamlit as st
from view import API

sidebar = st.sidebar
sidebar.selectbox(label='language', key='language', options=API.LANGUAGE, index=17)

all_playcard = API.playcard(st.session_state.language)
all_playcard = all_playcard['data']
sidebar.selectbox(label='Playcard', key='playcard', options=[_['displayName'] for _ in all_playcard])
for _ in all_playcard:
    if _['displayName'] == st.session_state.playcard:
        current_playcard = _

st.title(current_playcard['displayName'])
st.image(current_playcard['displayIcon'])
st.image([current_playcard['largeArt']])
sidebar.json(_)