import streamlit as st
from app.database.user_auth import create_user

st.markdown("""
    <style>
    .main-auth-card {
        max-width: 260px;
        margin: 3.5rem auto 1.2rem auto;
        background: var(--card-background);
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        padding: 1.2rem 1rem 1rem 1rem;
        text-align: center;
        color: var(--text-color);
        border: 1.2px solid var(--border-color);
    }
    .main-auth-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.7rem;
        color: var(--header-text);
        letter-spacing: 0.5px;
    }
    .main-auth-icon {
        font-size: 1.5rem;
        margin-bottom: 0.3rem;
        color: var(--primary-color);
    }
    .main-auth-link {
        color: var(--header-text);
        font-weight: 500;
        text-decoration: underline;
        cursor: pointer;
        font-size: 1.05rem;
    }
    .stTextInput > div > div > input {
        font-size: 0.95rem;
        padding: 0.4rem 0.7rem;
        border-radius: 7px;
        border: 1.5px solid var(--border-color);
        background-color: var(--input-background);
        color: var(--text-color);
        margin-bottom: 0.3rem;
        width: 92% !important;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
    .stButton > button {
        background: linear-gradient(120deg, var(--button-gradient-start), var(--button-gradient-end));
        color: var(--button-text);
        padding: 0.5rem 1.2rem;
        border-radius: 7px;
        border: none;
        font-weight: 600;
        font-size: 0.98rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
        width: 92%;
        margin: 0.4rem auto 0.1rem auto;
        display: block;
    }
    .stButton > button:hover {
        background: linear-gradient(120deg, var(--button-gradient-end), var(--button-gradient-start));
        color: var(--button-text);
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.10);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-auth-card">', unsafe_allow_html=True)
st.markdown('<div class="main-auth-icon">📝</div>', unsafe_allow_html=True)
st.markdown('<div class="main-auth-title">Sign Up</div>', unsafe_allow_html=True)

with st.form("signup_form", clear_on_submit=False):
    first_name = st.text_input('First Name', key='signup_first_name')
    last_name = st.text_input('Last Name', key='signup_last_name')
    username = st.text_input('Username', key='signup_username')
    email = st.text_input('Email', key='signup_email')
    password = st.text_input('Create Password', type='password', key='signup_password')
    signup_clicked = st.form_submit_button('Sign Up', use_container_width=True)

    if signup_clicked:
        if all([first_name, last_name, username, email, password]):
            success = create_user(first_name, last_name, username, email, password)
            if success:
                st.success('Account created! Please log in.')
                st.markdown('Go to <span class="main-auth-link">Login page</span>', unsafe_allow_html=True)
            else:
                st.error('Username or email already exists.')
        else:
            st.warning('Please fill in all fields.')

st.markdown('</div>', unsafe_allow_html=True) 