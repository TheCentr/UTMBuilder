#Url builder

import pandas as pd
import streamlit as st
import pyperclip

st.markdown("# The Centr - Add UTMs to your URL 🎈")

if st.checkbox('I am here to create my personal Omni-Support URL'):
    #st.text_input("Enter the original (naked) URL", key="ogurl", placeholder='For example: https://thecentr.com/teamsourcing', value='https://thecentr.com/teamsourcing')
    st.session_state.ogurl = 'https://thecentr.com/teamsourcing'

    #option = st.selectbox('Please select a source', ('facebook', 'youtube', 'linkedin', 'instagram', 'directsocialmessage'))
    st.session_state.source = 'directsocialmessage'

    #option2 = st.selectbox('Please select a medium', ('cpc', 'organic', 'banner', 'email', 'socialmessage'))
    #st.session_state.medium = 'socialmessage'

    #option3 = st.selectbox('Please select a campaign', ('teamsourcing', 'other'))
    st.session_state.campaign = 'teamsourcing'

    st.text_input("What is your username", key="medium", placeholder='For example: cwatson')

    st.markdown("#### After fill out the required information, copy this link")

    if st.button('Display URL'):
        st.write(f'{st.session_state.ogurl}?utm_source={st.session_state.source}&utm_medium={st.session_state.medium}&utm_campaign={st.session_state.campaign}&utm_content=none')

        st.markdown('## Instructions')
        st.write("Copy this link somewhere where you will always have access. When reffering someone to The Centr's landing page, use this link. Not the generic original link.")

    # if st.button('Copy URL'):
    #     text_to_be_copied = f'{st.session_state.ogurl}?utm_source={st.session_state.source}&utm_medium={st.session_state.medium}&utm_campaign={st.session_state.campaign}&utm_content={st.session_state.ad_id}'
    #     pyperclip.copy('test')
    #     st.write('Link copied!')


else:
    st.warning('Click the checkbox if you are here from omni-support')
    st.text_input("Enter the original (naked) URL", key="ogurl", placeholder='For example: https://thecentr.com/teamsourcing', value='https://thecentr.com/teamsourcing')

    option = st.selectbox('Please select a source', ('facebook', 'youtube', 'linkedin', 'instagram', 'direct'))
    st.session_state.source = option

    option2 = st.selectbox('Please select a medium', ('cpc', 'organic', 'banner', 'email', 'socialmessage'))
    st.session_state.medium = option2

    option3 = st.selectbox('Please select a campaign', ('teamsourcing', 'other'))
    st.session_state.campaign = option3

    st.text_input("What is the content name", key="ad_id")

    st.markdown("#### After fill out the required information, copy this link")

    if st.button('Display URL'):
        st.write(f'{st.session_state.ogurl}?utm_source={st.session_state.source}&utm_medium={st.session_state.medium}&utm_campaign={st.session_state.campaign}&utm_content={st.session_state.ad_id}')

    # if st.button('Copy URL'):
    #     text_to_be_copied = f'{st.session_state.ogurl}?utm_source={st.session_state.source}&utm_medium={st.session_state.medium}&utm_campaign={st.session_state.campaign}&utm_content={st.session_state.ad_id}'
    #     pyperclip.copy('test')
    #     st.write('Link copied!')
