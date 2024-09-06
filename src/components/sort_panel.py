import streamlit as st


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
