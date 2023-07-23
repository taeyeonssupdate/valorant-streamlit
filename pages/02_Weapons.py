import streamlit as st
from view import API

sidebar = st.sidebar
sidebar.selectbox(label='language', key='language', options=API.LANGUAGE, index=17)

all_weapons = API.weapons(st.session_state.language)
all_weapons = all_weapons['data']

sidebar.selectbox(label='weapons', key='select_weapons', options=[_['displayName'] for _ in all_weapons], index=2)
for _ in all_weapons:
    if _['displayName'] == st.session_state.select_weapons:
        current_weapons = _
        break
sidebar.selectbox(label='skin', key='select_skin', options=[_['displayName'] for _ in current_weapons['skins']])
for skin in current_weapons['skins']:
    if skin['displayName'] == st.session_state.select_skin:
        st.title(skin['displayName'])
        if skin.get('wallpaper'):
            st.image(skin['wallpaper'])
        if skin.get('displayIcon'):
            st.image(skin['displayIcon'])
        level_tab = st.tabs([_['displayName'] for _ in skin['levels']])
        for i, level in enumerate(skin['levels']):
            if level.get('displayIcon'):
                level_tab[i].image(level['displayIcon'])
            elif level.get('streamedVideo'):
                level_tab[i].video(level['streamedVideo'])
        chromas_tab = st.tabs([_['displayName'] for _ in skin['chromas']])
        for i, chroma in enumerate(skin['chromas']):
            chromas_tab[i].image(chroma['fullRender'])
        sidebar.json(skin)
        break
