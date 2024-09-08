import streamlit as st

from src.statics_enums import edition_mapping


def filter_options(df):
    edition = st.multiselect(
        "Edition",
        options=list(edition_mapping.values()),
        default=[edition_mapping.get(10)]
    )

    df = df[df['edition_name'].isin(edition)]

    # Create filter options for each column
    with st.expander("Filtering"):

        # First row: "Name" filter
        name_filter = st.multiselect(
            "Name",
            options=df['name'].unique()
        )

        col1, col2 = st.columns(2)
        with col1:
            rarity_filter = st.multiselect(
                "Rarity",
                options=df['rarity_name'].unique()
            )
        with col2:
            gold_filter = st.multiselect(
                "Foil",
                options=['Regular Foil', 'Gold Foil']
            )

        if name_filter:
            df = df[df['name'].isin(name_filter)]
        if rarity_filter:
            df = df[df['rarity_name'].isin(rarity_filter)]
        if gold_filter:
            gold = gold_filter == 'Gold Foil'
            df = df[df['gold'].isin(gold)]

    return df
