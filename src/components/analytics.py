import streamlit as st
import pandas as pd
import plotly.express as px

def render_analytics():

    st.subheader(
        "📊 Weekly Progress"
    )

    data = pd.DataFrame({
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],

        "Score": [
            65,
            78,
            82,
            90,
            88,
            95,
            91
        ]
    })

    fig = px.line(
        data,
        x="Day",
        y="Score",
        markers=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )