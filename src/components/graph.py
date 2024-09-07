import plotly.graph_objects as go
import streamlit as st

from src.statics_enums import rarity_colors, rarity_order

group_columns = ['edition', 'edition_name', 'rarity', 'rarity_name']


def add_rarity_distribution_graph(df, title):
    df = df.groupby(group_columns).agg({
        'num_cards': 'sum',
        'num_burned': 'sum'
    }).reset_index()
    st.plotly_chart(go.Figure(
        data=[
            go.Bar(
                x=df[df['rarity_name'] == rarity]['edition_name'],
                y=df[df['rarity_name'] == rarity]['num_cards'],
                name=rarity,
                marker=dict(color=rarity_colors[rarity])
            )
            for rarity in rarity_order
        ],
        layout=go.Layout(
            title=title,
            xaxis={'title': 'Edition'},
            yaxis={'title': 'Number of Cards'}

        )
    ))
