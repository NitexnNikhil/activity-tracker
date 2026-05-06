import streamlit as st

def render_theme_switcher():

    st.subheader(
        "🎨 Themes"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("🌑 Dark")

    with col2:
        st.button("🌸 Beige")

    with col3:
        st.button("⚡ Neon")