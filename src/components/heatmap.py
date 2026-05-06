import streamlit as st
import pandas as pd
import plotly.express as px
import random

def render_heatmap():

    st.subheader(
        "🔥 Consistency Heatmap"
    )

    days = []

    for i in range(1, 31):

        days.append({
            "Day": f"May-{i}",
            "Score": random.randint(0, 100)
        })

    df = pd.DataFrame(days)

    fig = px.density_heatmap(
        df,
        x="Day",
        y=["Activity"] * len(df),
        z="Score",
        color_continuous_scale="Viridis"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )