import streamlit as st
from pathlib import Path

from components.tracker import (
    render_tracker
)

from components.analytics import (
    render_analytics
)

from components.streak import (
    render_streak
)

from components.themes import (
    render_theme_switcher
)

st.set_page_config(
    page_title="✨ Daily Reset Tracker",
    layout="wide",
)

css_path = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "styles.css"
)
with open(
    css_path
) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

st.title(
    "✨ Daily Reset Tracker"
)

render_theme_switcher()

st.markdown("---")

render_streak()

st.markdown("---")

render_tracker()

st.markdown("---")

render_analytics()