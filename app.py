import streamlit as st
from login import login
from home import home
from about import about

def main():

    page = st.sidebar.selectbox('Page', ['Home', 'About'])

    if 'is_login' not in st.session_state:
        st.session_state.is_login = False

    if not st.session_state.is_login: 
        result = login()
        if result:
            st.session_state.is_login = True
            st.rerun()            
    else:
        if page == 'Home':
            home()
        elif page == 'About':
            about()


if __name__ == '__main__':
    main()