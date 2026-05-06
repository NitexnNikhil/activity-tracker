import streamlit as st
from pathlib import Path
from components.heatmap import render_heatmap
from components.calendar_view import render_calendar
from components.ai_score import render_ai_score
from components.mood import render_mood
from components.quotes import render_quote
from components.monk_mode import render_monk_mode
from components.detox import render_detox
from components.weekly_report import render_weekly_report

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

render_quote()

st.markdown("---")

render_ai_score()

st.markdown("---")

render_calendar()

st.markdown("---")

render_heatmap()

st.markdown("---")

render_mood()

st.markdown("---")

render_detox()

st.markdown("---")

render_monk_mode()

st.markdown("---")

render_weekly_report()