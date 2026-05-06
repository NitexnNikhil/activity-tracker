import streamlit as st
import random

def render_ai_score():

    score = random.randint(70, 98)

    st.subheader(
        "🤖 AI Productivity Score"
    )

    st.metric(
        "Today's Focus Level",
        f"{score}%"
    )

    if score > 90:

        st.success(
            "🔥 Main Character Energy"
        )

    elif score > 75:

        st.info(
            "⚡ Productive Day"
        )

    else:

        st.warning(
            "💤 Focus dropping"
        )