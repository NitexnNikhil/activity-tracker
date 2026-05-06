import streamlit as st
import plotly.express as px
import pandas as pd

def render_mood():

    st.subheader(
        "😊 Mood Analytics"
    )

    mood = st.slider(
        "Today's Mood",
        1,
        10,
        7
    )

    data = pd.DataFrame({
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri"
        ],

        "Mood": [
            6,
            8,
            7,
            9,
            mood
        ]
    })

    fig = px.line(
        data,
        x="Day",
        y="Mood",
        markers=True
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )