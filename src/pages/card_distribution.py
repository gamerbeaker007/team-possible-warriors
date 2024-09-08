import plotly.graph_objects as go
import streamlit as st

from src.statics_enums import edition_order, rarity_colors, rarity_order

group_columns = ['edition', 'edition_name', 'rarity', 'rarity_name']


def get_page(df):
    st.title("Distribution and Burned Totals by Edition and Rarity")
    combined_df = _get_combined_df(df)
    _add_total_distribution_graph(combined_df)

    # Show regular foil charts
    st.header("Regular Foil Cards Distribution")
    grouped_non_gold_df = _get_grouped_non_gold_df(df)
    _add_rarity_distribution_graph(grouped_non_gold_df, "Total Distribution by Edition and Rarity (Regular Foil)")
    _add_rarity_burned_graph(grouped_non_gold_df, "Total Burned by Edition and Rarity (Regular Foil)")

    st.header("Gold Foil Cards Distribution")
    grouped_gold_df = _get_grouped_gold_df(df)
    _add_rarity_distribution_graph(grouped_gold_df, "Total Distribution by Edition and Rarity (Gold Foil)")
    _add_rarity_burned_graph(grouped_gold_df, "Total Burned by Edition and Rarity (Gold Foil)")


def _get_grouped_non_gold_df(df):
    df_non_gold = df[df['gold'] == False]
    return df_non_gold.groupby(group_columns).agg({
        'num_cards': 'sum',
        'num_burned': 'sum',
        'unbound_cards': 'sum',
    }).reset_index()


def _get_grouped_gold_df(df):
    df_gold = df[df['gold'] == True]
    return df_gold.groupby(group_columns).agg({
        'num_cards': 'sum',
        'num_burned': 'sum',
        'unbound_cards': 'sum',
    }).reset_index()


def _get_combined_df(df):
    combined_df = df.groupby(group_columns).agg({
        'num_cards': 'sum',
        'num_burned': 'sum',
        'unbound_cards': 'sum'
    }).reset_index()

    combined_df['percent_burned'] = (combined_df['num_burned'] / combined_df['num_cards']) * 100

    return combined_df


def _add_rarity_distribution_graph(df, title):
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

    # Plot the chart with both types of bars
    st.plotly_chart(go.Figure(
        data=bars,
        layout=go.Layout(
            title=title,
            xaxis={'title': 'Edition'},
            yaxis={'title': 'Number of Cards'},
        )
    ))


def _add_total_distribution_graph(df):
    # Plot the total distribution chart
    st.plotly_chart(go.Figure(
        data=[
                 go.Bar(
                     x=[edition_name],
                     y=[df[df['edition_name'] == edition_name]['num_cards'].sum()],
                     name=edition_name,
                 ) for edition_name in edition_order
             ] + [
                 go.Bar(
                     x=['Soulbound Unbound'],  # Only for Soulbound
                     y=[df[df['edition_name'] == 'Soulbound']['unbound_cards'].sum()],
                     # Total unbound cards for Soulbound
                     name='Soulbound (Unbound Cards)',
                     marker=dict(color='green')  # Different color for distinction
                 )
             ]
        ,
        layout=go.Layout(
            title="Total Distribution by Edition",
            xaxis={'title': 'Edition'},
            yaxis={'title': 'Number of Cards'}

        )
    ))


def _add_rarity_burned_graph(df, title):
    # Plot the total distribution chart
    st.plotly_chart(go.Figure(
        data=[
            go.Bar(
                x=df[df['rarity_name'] == rarity]['edition_name'],
                y=df[df['rarity_name'] == rarity]['num_burned'],
                name=rarity,
                marker=dict(color=rarity_colors[rarity])
            )
            for rarity in rarity_order
        ],
        layout=go.Layout(
            title=title,
            xaxis={'title': 'Edition'},
            yaxis={'title': 'Number of Cards BURNED'}

        )
    ))
