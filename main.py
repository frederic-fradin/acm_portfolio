import streamlit as st

st.set_page_config(
    page_title="MarketData - Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# User credentials
USER_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2"
}

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            main.main()
        else:
            st.error("Invalid username or password")

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.sidebar.title(f"Welcome, {st.session_state.username}")
        st.sidebar.header("Menu")
        menu = ["Home"]
        choice = st.sidebar.selectbox("Go to", menu)
        if choice == "Home":
            from page import home
            home.main()
    else:
        login()

if __name__ == "__main__":
    main()
