from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

url = os.getenv("AUTH_URL") + "?"
url += "scope=openid&"
url += "response_type=code&"
url += f"client_id={os.getenv("CLIENT_ID")}&"
url += f"redirect_uri={os.getenv("REDIRECT_URL")}"

html_button = """
<style>
    .btn {
    background-color:#4169E1;
    color: #fff;
    border:none; 
    border-radius:10px; 
    padding:15px;
    min-height:30px; 
    width: 100%;
  }
</style>
"""
html_button += f'<a href="{url}" target="_self"><button class="btn" >Login</button></a>'

# st.subheader("Step 1: Initialize the flow", divider="grey")
st.markdown(html_button, unsafe_allow_html=True)

# st.subheader("Step 2: Redirect to keycloak", divider="grey")
# st.code(url.replace("&", "&\n"))