import plotly.graph_objects as go
import streamlit as st

from src.statics_enums import rarity_colors, rarity_order

group_columns = ['edition', 'edition_name', 'rarity', 'rarity_name']


def add_rarity_distribution_graph(df, title, print_unbounded=False):
    df = df.groupby(group_columns).agg({
        'num_cards': 'sum',
        'num_burned': 'sum',
        'unbound_cards': 'sum',
    }).reset_index()

    # List to hold all bars
    bars = []

    # Create bars for 'num_cards'
    for rarity in rarity_order:
        bars.append(
            go.Bar(
                x=df[df['rarity_name'] == rarity]['edition_name'],
                y=df[df['rarity_name'] == rarity]['num_cards'],
                name=f'{rarity} (Cards)',
                marker=dict(color=rarity_colors[rarity])
            )
        )
        if print_unbounded:
            unbound_df = df[df['rarity_name'] == rarity]
            if unbound_df['unbound_cards'].sum() > 0:  # Check if there are any unbound cards
                bars.append(
                    go.Bar(
                        x=unbound_df['edition_name'],
                        y=unbound_df['unbound_cards'],
                        name=f'{rarity} (Unbound Cards)',
                        marker=dict(color=rarity_colors[rarity], opacity=0.5)  # Different opacity for distinction
                    )
                )

    # Plot the chart with both types of bars
    st.plotly_chart(go.Figure(
        data=bars,
        layout=go.Layout(
            title=title,
            xaxis={'title': 'Edition'},
            yaxis={'title': 'Number of Cards'},
        )
    ))
