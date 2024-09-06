import streamlit as st

from src.components import sort_panel, filter_panel, total_card_header
from src.util import image_util

image_base_url = "https://images.hive.blog/125x0/https://d36mxiodymuqjm.cloudfront.net/cards_by_level/soulbound/"


def get_page(df):
    st.title("Rebellion Soulbound Edition - Distributed vs Unbound Percentage")

    df = _get_soulbound_df(df)
    columns = {
        'image_url': 'Image URL',
        'name': 'Name',
        'rarity_name': 'Rarity',
        'gold': 'Gold',
        'percent_unbound': 'Percent Unbound',
        'num_cards': 'Number of Cards',
        'unbound_cards': 'Number of Unbound Cards'
    }
    df.rename(columns=columns, inplace=True)

    df = filter_panel.filter_options(df, list(columns.values()))
    df = sort_panel.sort_options(df, list(columns.values()))

    df = df.drop('Gold', axis=1)

    total_card_header.add_totals_header(df)

    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)


def _get_soulbound_df(df):
    soulbound_df = df[df['edition_name'] == 'Soulbound Rebellion'].copy()
    soulbound_df['percent_unbound'] = ((soulbound_df['unbound_cards'] / soulbound_df['num_cards']) * 100).round(2)
    soulbound_df['image_url'] = soulbound_df.apply(image_util.generate_image_url, axis=1)
    return soulbound_df
