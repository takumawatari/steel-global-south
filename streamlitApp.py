import os
import streamlit as st

st.set_page_config(layout="wide")
st.title("Iron and steel flows in the Global South", anchor=None)

st.markdown("**Author**: [Takuma Watari](https://takuma-watari.com/en/) (National Institute for Environmental Studies, Japan)")

# Define available year
year = 2019  

# Define country list
country_list = [
    'Argentina', 'Chile', 'Colombia', 'Ecuador', 'Peru',
    'Algeria', 'Angola', 'Ghana', 'Kenya', 'Morocco', 'Nigeria', 'Tanzania',
    'Malaysia', 'Philippines', 'Thailand', 'Vietnam'
]
country = st.selectbox('Select Country', country_list)

# Construct file path
sankey_file_path = f"sankey/{country}_{year}.svg"

# Check if file exists before loading
if os.path.exists(sankey_file_path):
    with open(sankey_file_path, encoding="utf8") as file:
        svg_content = file.read()
    
    st.markdown(
        f'<div style="display: flex; justify-content: center;">{svg_content}</div>',
        unsafe_allow_html=True
    )
else:
    st.warning(f"File not found: {sankey_file_path}. Please check if the file exists.")
