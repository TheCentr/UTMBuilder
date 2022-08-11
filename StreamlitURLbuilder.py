#Url builder

import pandas as pd
import streamlit as st

st.write("The Centr - Add UTMs to your URL")



option = st.selectbox('Please select a brand', ('facebook', 'youtube', 'linkedin'))
st.session_state.brand = option

option2 = st.selectbox('Please select a medium', ('cpc', 'organic', 'banner'))
st.session_state.medium = option2

option3 = st.selectbox('Please select a campaign', ('teamsourcing'))
st.session_state.campaign = option3

st.text_input("What is the ad name", key="ad_id")


