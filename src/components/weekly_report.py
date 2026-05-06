import streamlit as st

def render_weekly_report():

    st.subheader(
        "📊 Weekly Reset Report"
    )

    st.info(
        '''
        ✅ Best Day: Thursday
        🔥 Longest Streak: 12 Days
        ⚠️ Cheat Days: 2
        🧘 Monk Mode Days: 4
        📵 Avg Detox Score: 82%
        '''
    )