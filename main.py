import streamlit as st
from st_pages import get_nav_from_toml, add_page_title

from src import data_util
from src.api import spl
from src.pages import card_distribution_page, unbounded_soulbound_page

st.set_page_config(page_title="Splinterlands Card Distribution", layout="wide")

# Fetch data
data = spl.get_card_details()
df = data_util.preprocess_data(data)

nav = get_nav_from_toml('.streamlit/pages.toml')

pg = st.navigation(nav)

add_page_title(pg)

# Dynamically call the page-specific function based on the selected page
if pg.title == "Card Distribution":
    card_distribution_page.card_distribution_page(df)
elif pg.title == "Unbounded Soulbound":
    unbounded_soulbound_page.unbounded_soulbound_page(df)

pg.run()
