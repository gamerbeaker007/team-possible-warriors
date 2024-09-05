import streamlit as st

from src.statics_enums import rarity_to_level

image_base_url = "https://images.hive.blog/125x0/https://d36mxiodymuqjm.cloudfront.net/cards_by_level/soulbound/"


def unbounded_soulbound_page(df):
    st.title("Soulbound Edition - Distributed vs Unbound Percentage")

    df = get_soulbound_df(df)
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

    df = filter_options(df, list(columns.values()))
    df = sort_options(df, list(columns.values()))

    df = df.drop('Gold', axis=1)

    # Display the dataframe as HTML with images
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)


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


def sort_options(df, columns):
    columns.remove('Image URL')
    columns.remove('Gold')

    with st.expander("Sorting", expanded=True):  # Collapsible panel with the title 'Sorting'
        col1, col2 = st.columns([2, 1])  # Two columns, adjust the width ratio as needed

        with col1:
            # Input field for sorting column
            sort_column = st.selectbox("Select column to sort by", options=columns)

        with col2:
            # Input field for sorting order
            sort_order = st.radio("Sort order", options=["Ascending", "Descending"])

        # Sorting the dataframe based on inputs
        ascending = sort_order == "Ascending"
        df = df.sort_values(by=sort_column, ascending=ascending)

    return df


def get_soulbound_df(df):
    soulbound_df = df[df['edition_name'] == 'Soulbound'].copy()
    soulbound_df['percent_unbound'] = ((soulbound_df['unbound_cards'] / soulbound_df['num_cards']) * 100).round(2)
    soulbound_df['image_url'] = soulbound_df.apply(generate_image_url, axis=1)
    return soulbound_df


def generate_image_url(row):
    card_name = row['name'].replace(' ', '%20')  # Replace spaces with %20
    level = rarity_to_level[row['rarity_name']]
    markdown_prefix = "![" + str(card_name) + "]"

    if row['gold']:
        img_url = f"{image_base_url}{card_name}_lv{level}_gold.png"
    else:
        img_url = f"{image_base_url}{card_name}_lv{level}.png"

    return f'<img src="{img_url}" width="60">'
