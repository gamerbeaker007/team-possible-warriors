import logging

import numpy as np
import streamlit as st

from src.api import spl


def get_page():
    st.title("Team possible warriors - Contributions ")
    guild_id = spl.get_guild_id('Team Possible Warriors')
    st.header(f'Guild id: {guild_id}')
    df = spl.get_guild_members_df(guild_id)
    df = add_percent_column(df, 'warriorsfund')

    num_columns = 4
    rows_per_column = (len(df) + num_columns - 1) // num_columns  # Calculate rows per column, rounded up

    # Create 4 columns in Streamlit
    columns = st.columns(num_columns)

    # Loop through each column and assign a chunk of the DataFrame
    for i, col in enumerate(columns):
        start_idx = i * rows_per_column
        end_idx = start_idx + rows_per_column
        col.dataframe(df[['player', 'percent', 'valid']].iloc[start_idx:end_idx])


def add_percent_column(df, fund_account_name):
    # Add columns with default values
    df['percent'] = 0
    df['valid'] = False

    for index, row in df.iterrows():
        delegate_to_player = row['player']

        contributions = spl.get_contributions(delegate_to_player)
        for contribution in contributions:
            if (contribution['delegate_to_player'] == fund_account_name and
                    contribution['type'] == 'brawl' and
                    contribution['token'] == 'SPS'):
                percentage = float(contribution['percent'])
                df.at[index, 'percent'] = percentage
                if percentage >= 25.0:
                    df.at[index, 'valid'] = True

    return df
