import streamlit as st

def check_data(username, password):
    user = st.secrets['login']['user']
    passw = st.secrets['login']['password']
    if username == user and password == passw:
        return True
    else:
        st.error('Username or password error')
def login():
    st.subheader("Login to your account")
    username = st.text_input('User Name', "", placeholder='enter your username')
    password = st.text_input('Password',"", type="password", placeholder='enter your password')
    if st.button("Login"):
        return check_data(username, password)
