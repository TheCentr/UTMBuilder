#Url builder

import pandas as pd
import streamlit as st

st.markdown("# The Centr - Add UTMs to your URL 🎈")

st.text_input("Enter the original (naked) URL", key="ogurl")

option = st.selectbox('Please select a source', ('facebook', 'youtube', 'linkedin', 'instagram'))
st.session_state.brand = option

option2 = st.selectbox('Please select a medium', ('cpc', 'organic', 'banner', 'email'))
st.session_state.medium = option2

option3 = st.selectbox('Please select a campaign', ('teamsourcing', 'other'))
st.session_state.campaign = option3

st.text_input("What is the content name", key="ad_id")


st.write(f'{st.session_state.ogurl}?utm_source={st.session_state.brand}+&utm_medium={st.session_state.medium}+&utm_campaign={st.session_state.campaign}+&utm_content={st.session_state.ad_id}')


