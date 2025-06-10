import streamlit as st
from app.database.user_auth import validate_user

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

if st.session_state.get('logged_in', False):
    st.success('Login successful!')
    st.stop()

st.markdown('<div class="main-auth-card">', unsafe_allow_html=True)
st.markdown('<div class="main-auth-icon">🔐</div>', unsafe_allow_html=True)
st.markdown('<div class="main-auth-title">Login</div>', unsafe_allow_html=True)

with st.form("login_form", clear_on_submit=False):
    username = st.text_input('Username', key='login_username')
    password = st.text_input('Password', type='password', key='login_password')
    login_clicked = st.form_submit_button('Login', use_container_width=True)

    if login_clicked:
        if validate_user(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful!')
            st.rerun()
        else:
            st.error('Invalid username or password.')

st.markdown('</div>', unsafe_allow_html=True) 