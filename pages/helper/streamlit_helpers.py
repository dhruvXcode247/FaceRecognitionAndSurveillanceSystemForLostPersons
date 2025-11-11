import streamlit as st
from functools import wraps


def require_login(func):
    if "login_status" not in st.session_state or not st.session_state["login_status"]:
        st.warning("⚠️ Please log in first from the Home page to access this section.")
        st.stop()


def show_success(message: str):
    st.success(message)


def show_error(message: str):
    st.error(message)


def show_warning(message: str):
    st.warning(message)
