import streamlit as st
from pages.helper import db_queries

st.set_page_config(page_title="Missing Person Finder", layout="centered")

# -----------------------------
# Simple Login System
# -----------------------------
st.title("🔐 Login")

if "login_status" not in st.session_state:
    st.session_state["login_status"] = False

if not st.session_state["login_status"]:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # 💡 You can add more users here
        valid_users = {
            "admin": "1234",
            "dhruv": "5678",
        }

        if username in valid_users and password == valid_users[username]:
            st.session_state["login_status"] = True
            st.session_state["user"] = username
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")
else:
    st.sidebar.success(f"Welcome, {st.session_state['user']}!")
    if st.sidebar.button("Logout"):
        st.session_state["login_status"] = False
        st.rerun()

    st.markdown("---")
    st.subheader("📊 Case Summary")

    user = st.session_state["user"]
    found_cases = db_queries.get_registered_cases_count(user, "F")
    non_found_cases = db_queries.get_registered_cases_count(user, "NF")

    col1, col2 = st.columns(2)
    col1.metric("Found Cases", len(found_cases))
    col2.metric("Not Found Cases", len(non_found_cases))

    st.markdown("---")
    st.success("You are logged in! Access other pages from the sidebar.")
