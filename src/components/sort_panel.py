import streamlit as st


def sort_options(df, columns):
    columns.remove('Image URL')

    with st.expander('Sorting'):  # Collapsible panel with the title 'Sorting'
        col1, col2 = st.columns([2, 1])  # Two columns, adjust the width ratio as needed

        with col1:
            # Input field for sorting column
            sort_column = st.selectbox(
                'Select column to sort by',
                options=columns,
                index=columns.index('Number of Cards')
            )

        with col2:
            # Input field for sorting order
            sort_order = st.radio(
                'Sort order',
                options=['Ascending', 'Descending'],
                index=1
            )

        ascending = sort_order == 'Ascending'
        df = df.sort_values(by=sort_column, ascending=ascending)

    return df
