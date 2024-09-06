import pandas as pd

from src.statics_enums import rarity_mapping, edition_mapping


def preprocess_data(data):
    df = get_all_distributions_df(data)
    df = make_columns_as_int(df)
    df = add_rarity_names(df)
    df = add_edition_names(df)
    return df


def get_all_distributions_df(df):
    # Prepare and process data (same as in Dash code)
    all_distributions = []
    for index, row in df.iterrows():
        for dist in row['distribution']:
            dist['name'] = row['name']
            dist['rarity'] = row['rarity']
            all_distributions.append(dist)

    df = pd.DataFrame(all_distributions)
    return df


def make_columns_as_int(df):
    df['num_cards'] = df['num_cards'].astype(int)
    df['num_burned'] = df['num_burned'].astype(int)
    df['unbound_cards'] = df['unbound_cards'].astype(int)
    return df


def add_rarity_names(df):
    df['rarity_name'] = df['rarity'].map(rarity_mapping)
    return df


def add_edition_names(df):
    df['edition_name'] = df['edition'].map(edition_mapping)
    return df