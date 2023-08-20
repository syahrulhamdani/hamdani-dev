import streamlit as st

import kodedata.config as c


st.set_page_config(**c.PAGES_CONFIG["dashboard"])
st.title("YouTube Trending Video Statistics Dashboard")
