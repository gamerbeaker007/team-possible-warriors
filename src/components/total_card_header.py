import streamlit as st


def add_totals_header(df):
    col1, col2, col3 = st.columns(3)
    with col1:
        total = df['num_cards'].sum()
        st.markdown("""
        ### Total Cards:
        """ + f"{total:,.0f}")
    with col2:
        total_burned = df['num_burned'].sum()
        st.markdown("""
        ### Total Burned Cards:
        """ + f"{total_burned:,.0f}")
    with col3:
        total_unbound = df['unbound_cards'].sum()
        st.markdown("""
        ### Total Unbounded Cards:
        """ + f"{total_unbound:,.0f}")

    col1, col2, col3 = st.columns(3)
    with col1:
        total = df['bcx'].sum()
        st.markdown("""
        ### Total BCX (circulating):
        """ + f"{total:,.0f}")
    with col2:
        total_burned = df['burned_bcx'].sum()
        st.markdown("""
        ### Total Burned BCX:
        """ + f"{total_burned:,.0f}")
    with col3:
        st.markdown("")
