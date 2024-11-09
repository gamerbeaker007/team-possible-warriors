import streamlit as st

from src.api import spl

guild_name = 'Team Possible Warriors'
fund_account_name = 'warriorsfund'
reward_percentage = 25.0


def get_page():
    st.title('Team possible warriors - Contributions ')
    if st.button('Refresh Data'):
        st.cache_data.clear()

    guild_id = spl.get_guild_id(guild_name)
    st.markdown(f"""
        <div style="font-size: 1.2em;">
            <p><strong>Guild ID:</strong> {guild_id} </br>
            The reward delegations to <strong>"{fund_account_name}"</strong> are presented for each member below.<br />
            <em>Note:</em> An account is valid when the delegation is <strong>&ge; {reward_percentage}%</strong>.<br />
            </p>
        </div>
    """, unsafe_allow_html=True)

    with st.spinner('Loading data...'):
        df = spl.get_guild_members_df(guild_id)
        df = add_percent_column(df, fund_account_name)

    num_columns = 4
    rows_per_column = (len(df) + num_columns - 1) // num_columns  # Calculate rows per column, rounded up

    # Create 4 columns in Streamlit
    columns = st.columns(num_columns)

    # Loop through each column and assign a chunk of the DataFrame
    for i, col in enumerate(columns):
        start_idx = i * rows_per_column
        end_idx = start_idx + rows_per_column
        col.dataframe(df[['player', 'percent', 'valid']].iloc[start_idx:end_idx])


def add_percent_column(df, requested_delegation_account):
    # Add columns with default values
    df['percent'] = 0
    df['valid'] = False

    for index, row in df.iterrows():
        delegate_to_player = row['player']

        contributions = spl.get_contributions(delegate_to_player)
        for contribution in contributions:
            if (contribution['delegate_to_player'] == requested_delegation_account and
                    contribution['type'] == 'brawl' and
                    contribution['token'] == 'SPS'):
                percentage = float(contribution['percent'])
                df.at[index, 'percent'] = percentage
                if percentage >= reward_percentage:
                    df.at[index, 'valid'] = True

    return df
