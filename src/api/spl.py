import logging

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


@st.cache_data(ttl='24h')
def get_guild_id(name):
    params = {'name': name}
    address = base_url + 'guilds/list'
    response = http.get(address, params=params).json()

    guilds = response.get('guilds', [])

    if not guilds:
        return None
    elif len(guilds) > 1:
        logging.warning(f'Multiple guilds found for name {name}')
        return None
    else:
        return guilds[0].get('id')


@st.cache_data(ttl='24h')
def get_guild_members_df(guild_id):
    params = {'guild_id': guild_id}
    address = base_url + 'guilds/members'
    df = pd.DataFrame(http.get(address, params=params).json())
    return df.loc[df.status == 'active']


@st.cache_data(ttl='1h')
def get_contributions(username):
    params = {'username': username}
    url = base_url + '/players/reward_delegations'
    response = requests.get(url, params=params)
    return response.json()
