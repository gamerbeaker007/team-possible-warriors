import streamlit as st


def filter_options(df, columns):
    # Create filter options for each column
    with st.expander("Filtering", expanded=True):

        # First row: "Name" filter
        name_filter = st.multiselect("Name", options=df['Name'].unique())

        col1, col2 = st.columns(2)
        with col1:
            rarity_filter = st.multiselect("Rarity", options=df['Rarity'].unique())
        with col2:
            gold_filter = st.multiselect("Gold Foil", options=df['Gold'].unique())

        df = df[columns].copy()

        if name_filter:
            df = df[df['Name'].isin(name_filter)]
        if rarity_filter:
            df = df[df['Rarity'].isin(rarity_filter)]
        if gold_filter:
            df = df[df['Gold'].isin(gold_filter)]

    return df
