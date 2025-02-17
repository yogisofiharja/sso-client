from dotenv import load_dotenv
import jwt
import os
import requests
import streamlit as st

load_dotenv()

body = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "redirect_uri": os.getenv("REDIRECT_URL"),
        "grant_type": "authorization_code",
        "code": st.query_params["code"],
    }

resp = requests.post(
    os.getenv("TOKEN_URL"),
    data=body
)
resp_json = resp.json()

if resp.status_code == 200:
    # print(resp.json())

    # st.subheader("Code flow result", divider="grey")
    # st.write(resp.json())
    if "access_token" in resp_json:
        logout_button = """
        <style>
            .btn {
            background-color:rgb(127 31 32);
            color: #fff;
            border:none; 
            border-radius:10px; 
            padding:15px;
            min-height:30px; 
            width: 100%;
        }
        </style>
        """
        logout_button += f'<a href="{os.getenv("LOGOUT_URL")}" target="_self"><button class="btn" >Logout</button></a>'
        st.markdown(logout_button, unsafe_allow_html=True)

        access_token = resp_json["access_token"]

        # Decode the access token
        decoded_token = jwt.decode(access_token, options={"verify_signature": False})
        # st.write("Decoded Access Token:", decoded_token)
        # Check for roles in the decoded token
        roles = decoded_token.get("roles", [])
        if roles:
            # st.write("Roles:", roles)
            if any(role in roles for role in ["admin", "manager", "employee"]):
                st.success(f"{decoded_token["name"]} signed in to application {decoded_token["azp"]} as {', '.join(role for role in roles if role in ['admin', 'manager', 'employee'])}")
            else:
                st.error("User does not have a valid role")
        else:
            st.error("No roles found in the token")
    else:
        st.error("Invalid credentials: Access token not found")
else:
    st.error(f"Invalid credentials: {resp.status_code} - {resp_json["error_description"]}")


