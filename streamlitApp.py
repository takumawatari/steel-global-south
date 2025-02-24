import os
import streamlit as st

st.set_page_config(layout="wide")
st.title("Iron and steel flows in the Global South", anchor=None)

st.markdown("**Author**: [Takuma Watari](https://takuma-watari.com/en/) (National Institute for Environmental Studies, Japan)")

# available year
year = 2019  

# country list
country_list = [
    'Argentina', 'Chile', 'Colombia', 'Ecuador', 'Peru',
    'Algeria', 'Angola', 'Ghana', 'Kenya', 'Morocco', 'Nigeria', 'Tanzania',
    'Malaysia', 'Philippines', 'Thailand', 'Vietnam'
]
country = st.selectbox('**Select country:**', country_list)

# file path
sankey_file_path = f"sankey/{country}_{year}.svg"

# open
st.image(sankey_file_path)
