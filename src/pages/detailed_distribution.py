import streamlit as st

from src.components import sort_panel, filter_panel, total_card_header, graph
from src.util import image_util


def get_page(df):
    st.title("Detailed Cards Distributed ")

    df = _calculated_percent_unbound(df)
    df = _add_image_url(df)

    filtered_df = filter_panel.filter_options(df)

    columns = {
        'image_url': 'Image URL',
        'name': 'Name',
        'rarity_name': 'Rarity',
        'edition_name': 'Edition',
        'bcx': 'Number of BCX',
        'burned_bcx': 'Number of Burned BCX',
        'num_cards': 'Number of Cards',
        'num_burned': 'Number of Burned Cards',
        'unbound_cards': 'Number of Unbound Cards',
        'percent_unbound': 'Percent Unbound',
    }

    graph.add_rarity_distribution_graph(filtered_df, "Total distribution by rarity")

    total_card_header.add_totals_header(filtered_df)

    renamed_columns_df = filtered_df.rename(columns=columns)
    renamed_columns_df = renamed_columns_df[list(columns.values())].copy()
    renamed_columns_df = sort_panel.sort_options(renamed_columns_df, list(columns.values()))
    st.write(renamed_columns_df.to_html(escape=False, index=False), unsafe_allow_html=True)


def _calculated_percent_unbound(df):
    df['percent_unbound'] = ((df['unbound_cards'] / df['num_cards']) * 100).round(2)
    return df


def _add_image_url(df):
    df['image_url'] = df.apply(lambda row: image_util.generate_image_url(
        row['name'],
        row['rarity_name'],
        row['edition'],
        row['gold']
    ), axis=1)
    return df
