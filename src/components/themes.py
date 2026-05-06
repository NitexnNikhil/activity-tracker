import streamlit as st

THEMES = {

    "dark": """
    <style>
    .stApp {
        background: #0f0f0f;
        color: white;
    }
    </style>
    """,

    "beige": """
    <style>
    .stApp {
        background: #F5E6D3;
        color: #3E2C23;
    }

    h1,h2,h3,p,label {
        color: #3E2C23 !important;
    }

    div[data-testid="stCheckbox"] {
        background: rgba(255,255,255,0.7);
        border-radius: 16px;
        padding: 12px;
    }
    </style>
    """,

    "neon": """
    <style>
    .stApp {
        background: #0f0f0f;
        color: #00ffcc;
    }

    h1,h2,h3,p,label {
        color: #00ffcc !important;
    }

    div[data-testid="stCheckbox"] {
        background: rgba(0,255,200,0.08);
        border: 1px solid #00ffcc;
        border-radius: 16px;
        padding: 12px;
    }
    </style>
    """
}

def render_theme_switcher():

    st.subheader("🎨 Choose Theme")

    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌑 Dark"):
            st.session_state.theme = "dark"

    with col2:
        if st.button("🌸 Beige"):
            st.session_state.theme = "beige"

    with col3:
        if st.button("⚡ Neon"):
            st.session_state.theme = "neon"

    st.markdown(
        THEMES[st.session_state.theme],
        unsafe_allow_html=True
    )