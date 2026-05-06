import streamlit as st

from utils.constants import (
    MORNING_HABITS,
    PRODUCTIVITY_HABITS,
    MENTAL_HEALTH_HABITS,
    NIGHT_HABITS,
)

from utils.helpers import (
    save_habit,
    get_habits,
)

USER_ID = "nikky"

saved_habits = get_habits(USER_ID)

def render_section(title, habits):

    st.subheader(title)

    completed = 0

    for habit in habits:

        checked = st.checkbox(
            habit,
            value=saved_habits.get(habit) == "True"
        )

        save_habit(
            USER_ID,
            habit,
            checked
        )

        if checked:
            completed += 1

    percentage = int(
        (completed / len(habits)) * 100
    )

    st.progress(
        percentage / 100
    )

    st.write(
        f"✨ {percentage}% completed"
    )

def render_tracker():

    col1, col2 = st.columns(2)

    with col1:

        render_section(
            "🌅 Morning",
            MORNING_HABITS
        )

        render_section(
            "💻 Productivity",
            PRODUCTIVITY_HABITS
        )

    with col2:

        render_section(
            "🧠 Mental Health",
            MENTAL_HEALTH_HABITS
        )

        render_section(
            "🌙 Night Reset",
            NIGHT_HABITS
        )

    st.markdown("---")

    st.subheader("🎯 Main Character Goal")

    goal = st.text_input(
        "Today's Goal"
    )

    redis_goal_key = (
        f"user:{USER_ID}:goal"
    )

    from utils.redis_db import redis

    redis.set(
        redis_goal_key,
        goal
    )

    st.subheader("📝 Notes")

    notes = st.text_area(
        "Daily Notes"
    )

    redis.set(
        f"user:{USER_ID}:notes",
        notes
    )