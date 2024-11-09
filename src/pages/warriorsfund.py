import streamlit as st

from src.api import spl

fund_account_name = 'warriorsfund'


def get_page():
    st.title('Warriorsfund - Overview ')

    with st.spinner('Loading data...'):
        df = spl.get_balances_df(fund_account_name)
        pivot_df = df.pivot_table(index='player', columns='token', values='balance', aggfunc='first').reset_index()
        pivot_df = pivot_df.rename(columns={"SPSP": "Staked SPS"})
        st.dataframe(pivot_df.set_index(pivot_df.columns[0]))
