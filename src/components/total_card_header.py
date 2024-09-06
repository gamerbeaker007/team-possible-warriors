import streamlit as st


def add_totals_header(df):
    col1, col2 = st.columns(2)
    with col1:
        total = df['Number of Cards'].sum()
        st.subheader(f"Total Cards: {total:,.0f}")
    with col2:
        total_unbound = df['Number of Unbound Cards'].sum()
        st.subheader(f"Total Unbounded Cards: {total_unbound:,.0f}")
