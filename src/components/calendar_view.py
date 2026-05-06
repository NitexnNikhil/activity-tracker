import streamlit as st
from datetime import date

def render_calendar():

    st.subheader(
        "📅 Monthly Calendar"
    )

    selected = st.date_input(
        "Select Day",
        value=date.today()
    )

    st.success(
        f"Tracking: {selected}"
    )