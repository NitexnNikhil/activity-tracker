import streamlit as st

def render_streak():

    st.markdown(
        """
        <div style='
            padding:20px;
            border-radius:20px;
            background: linear-gradient(
                135deg,
                #ff0080,
                #7928ca
            );
            text-align:center;
            font-size:28px;
            font-weight:bold;
        '>
            🔥 12 Day Streak
        </div>
        """,
        unsafe_allow_html=True
    )