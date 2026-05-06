import streamlit as st

def render_monk_mode():

    st.subheader(
        "🧘 Monk Mode"
    )

    monk = st.toggle(
        "Enable Monk Mode"
    )

    if monk:

        st.success(
            "🔥 Monk Mode Activated"
        )

    else:

        st.warning(
            "⚠️ Distraction Mode"
        )