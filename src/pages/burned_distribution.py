import pandas as pd
import streamlit as st

from src.components import sort_panel, filter_panel, graph
from src.statics_enums import rarity_order, edition_mapping
from src.util import image_util


def get_page(df):
    st.title("Burned Cards Distributed ")

    df = _add_image_url(df)

    filtered_df = filter_panel.filter_options(df, edition_mapping.get(3))

    columns = {
        'image_url': 'Image URL',
        'name': 'Name',
        'rarity_name': 'Rarity',
        'edition_name': 'Edition',
        'bcx': 'Number of BCX',
        'burned_bcx': 'Number of Burned BCX',
        'num_cards': 'Number of Cards',
        'num_burned': 'Number of Burned Cards',
    }

    graph.add_burned_rarity_distribution_graph(filtered_df, "Total burned BCX by rarity")

    renamed_columns_df = filtered_df[list(columns.keys())].rename(columns=columns)

    st.header("Number of BCX")
    _add_pivot_rarity_table(renamed_columns_df, 'Number of BCX')
    st.header("Burned BCX")
    _add_pivot_rarity_table(renamed_columns_df, 'Number of Burned BCX')

    _add_totals_header(renamed_columns_df)

    renamed_columns_df = renamed_columns_df[list(columns.values())].copy()
    renamed_columns_df = sort_panel.sort_options(renamed_columns_df, list(columns.values()))
    st.write(renamed_columns_df.to_html(escape=False, index=False), unsafe_allow_html=True)


def _add_image_url(df):
    df['image_url'] = df.apply(lambda row: image_util.generate_image_url(
        row['name'],
        row['rarity_name'],
        row['edition'],
        row['gold']
    ), axis=1)
    return df


def _add_totals_header(df):
    col1, col2 = st.columns(2)
    with col1:
        total = df['Number of BCX'].sum()
        st.markdown("""
        ### Total BCX:
        """ + f"{total:,.0f}")
    with col2:
        total_burned = df['Number of Burned BCX'].sum()
        st.markdown("""
        ### Total Burned BCX:
        """ + f"{total_burned:,.0f}")


def _add_pivot_rarity_table(df, column):
    # Create a pivot table
    pivot_df = (
        pd.pivot_table(
            df,
            values=column,
            index='Edition',  # Rows
            columns='Rarity',  # Columns
            aggfunc='sum',  # Aggregate with sum
            fill_value=0
        ).reindex(columns=rarity_order)
        .reset_index()
    )

    st.dataframe(
        pivot_df,
        hide_index=True,
        column_config={
            "Edition": st.column_config.Column(width="2000px")  # Set width of Edition column
        },
        use_container_width=True  # Use container width for the rest of the columns
    )
