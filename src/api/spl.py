import pandas as pd
import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# Define URLs and retry strategy
base_url = 'https://api2.splinterlands.com/'

retry_strategy = Retry(
    total=10,
    status_forcelist=[429, 500, 502, 503, 504],
    backoff_factor=2,
    allowed_methods=['HEAD', 'GET', 'OPTIONS']
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount('https://', adapter)


@st.cache_data(ttl="1h")
def get_card_details():
    address = base_url + 'cards/get_details'
    return pd.DataFrame(http.get(address).json()).set_index('id')
