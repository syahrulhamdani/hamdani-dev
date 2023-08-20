"""Main app"""
import streamlit as st

import kodedata.config as c

st.set_page_config(**c.PAGES_CONFIG["home"])

st.image(c.LOGO_FILENAME)
st.title(c.APP_NAME)
