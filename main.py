import streamlit as st

from src import data_util
from src.api import spl
from src.pages import card_distribution_page, unbounded_soulbound_page

st.set_page_config(page_title="Splinterlands Card Distribution", layout="wide")

# Fetch data
data = spl.get_card_details()
df = data_util.preprocess_data(data)

# Pages Navigation
st.sidebar.title("Pages")
page = st.sidebar.radio("Go to", ["Card Distribution", "Unbounded Soulbound"])

if page == "Card Distribution":
    card_distribution_page.card_distribution_page(df)
elif page == "Unbounded Soulbound":
    unbounded_soulbound_page.unbounded_soulbound_page(df)
