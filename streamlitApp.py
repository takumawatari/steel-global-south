import pandas as pd
import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("Iron and steel flows in the Global South", anchor=None)

st.markdown("**Author**: [Takuma Watari](https://takuma-watari.com/en/) (National Institute for Environmental Studies, Japan)")

year = [2019]
file_path = os.path.join('data', f'data_{year}.xlsx')
country_list = ['Argentina','Chile','Colombia','Ecuador','Peru',
               'Algeria','Angola','Ghana','Kenya','Morocco','Nigeria','Tanzania',
               'Malaysia','Philippines','Thailand','Vietnam']
country = st.selectbox('Select country', country_list)

sankey_file_path = f"sankey/{country}_{year}.svg"
with open(sankey_file_path, encoding="utf8") as file:
        svg_content = file.read()
    st.markdown(f'<div style="justify-content: center;">{svg_content}</div>', unsafe_allow_html=True)
