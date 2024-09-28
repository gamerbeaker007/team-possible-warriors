import plotly.graph_objects as go
import streamlit as st

from src.statics_enums import rarity_colors, rarity_order

group_columns = ['edition', 'edition_name', 'rarity', 'rarity_name']


def add_rarity_distribution_graph(df, title):
    df = df.groupby(group_columns).agg({
        'num_cards': 'sum',
        'num_burned': 'sum',
        'unbound_cards': 'sum',
    }).reset_index()

    # List to hold all bars
    bars = []

    for edition in df['edition_name'].unique():
        edition_df = df[df['edition_name'] == edition]

        for rarity in rarity_order:
            rarity_df = edition_df[edition_df['rarity_name'] == rarity]

            bars.append(
                go.Bar(
                    x=rarity_df['edition_name'],
                    y=rarity_df['num_cards'],
                    name=f'{rarity}',
                    marker=dict(color=rarity_colors[rarity]),
                    legendgroup=rarity,
                    showlegend=(edition == df['edition_name'].unique()[0]),
                    xperiodalignment="middle"
                )
            )

            unbound_df = rarity_df[rarity_df['unbound_cards'] > 0]
            if not unbound_df.empty:
                bars.append(
                    go.Bar(
                        x=unbound_df['edition_name'],
                        y=unbound_df['unbound_cards'],
                        name=f'{rarity} (Unbound)',
                        marker=dict(color=rarity_colors[rarity], opacity=0.5),  # Different opacity for distinction
                        legendgroup=f'unbounded {rarity}',
                        xperiodalignment="middle"
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


def add_burned_rarity_distribution_graph(df, title):
    df = df.groupby(group_columns).agg({
        'num_cards': 'sum',
        'num_burned': 'sum',
        'burned_bcx': 'sum',
    }).reset_index()

    bars = []
    # Create bars for 'num_cards'
    for rarity in rarity_order:
        bars.append(
            go.Bar(
                x=df[df['rarity_name'] == rarity]['edition_name'],
                y=df[df['rarity_name'] == rarity]['burned_bcx'],
                name=f'{rarity}',
                marker=dict(color=rarity_colors[rarity])
            )
        )

    # Plot the chart with both types of bars
    st.plotly_chart(go.Figure(
        data=bars,
        layout=go.Layout(
            title=title,
            xaxis={'title': 'Edition'},
            yaxis={'title': 'Number burned BCX'},
        )
    ))
