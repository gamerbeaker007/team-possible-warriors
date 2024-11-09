import streamlit as st
from st_pages import get_nav_from_toml, add_page_title

from src.pages import contributions, warriorsfund

st.set_page_config(page_title='Splinterlands - Team Possible Warriors', layout='wide')

nav = get_nav_from_toml('.streamlit/pages.toml')

pg = st.navigation(nav)

add_page_title(pg)

# Dynamically call the page-specific function based on the selected page
if pg.title == 'Contributions':
    contributions.get_page()
elif pg.title == 'Warriorsfund':
    warriorsfund.get_page()

pg.run()
