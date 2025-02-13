import streamlit as st

from src.api import spl

fund_account_name = 'warriorsfund'


def get_page():
    st.title('Warriorsfund - Overview ')

    with st.spinner('Loading data...'):
        df = spl.get_balances_df(fund_account_name)
        pivot_df = df.pivot_table(index='player', columns='token', values='balance', aggfunc='first').reset_index()
        pivot_df = pivot_df.rename(columns={"SPSP": "Staked SPS"})
        st.dataframe(pivot_df.set_index(pivot_df.columns[0]), use_container_width=True)
        delegations = spl.get_outgoing_delegations(fund_account_name)
        st.markdown("### Warriors members that receive SPS delegation boost:")
        if not delegations.empty:
            st.markdown("\n".join(f"- {row.player} ({round(float(row.amount))} SPS)"
                                  for index, row in delegations.iterrows()))
        else:
            st.write("None")
