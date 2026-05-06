import streamlit as st

def render_detox():

    st.subheader(
        "📵 Phone Detox"
    )

    screen_time = st.slider(
        "Screen Time (hrs)",
        0,
        15,
        5
    )

    detox_score = max(
        0,
        100 - (screen_time * 6)
    )

    st.metric(
        "Detox Score",
        f"{detox_score}%"
    )

    if detox_score > 80:

        st.success(
            "🔥 Digital Discipline"
        )

    else:

        st.warning(
            "📱 Too much screen time"
        )