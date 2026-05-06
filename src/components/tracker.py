import streamlit as st
from datetime import date

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

def render_section(
    title,
    habits,
    selected_date,
    saved_habits
):

    st.subheader(title)

    completed = 0

    for habit in habits:

        checked = st.checkbox(
            habit,
            value=saved_habits.get(habit) == "True",
            key=f"{selected_date}-{habit}"
        )

        save_habit(
            USER_ID,
            selected_date,
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

    st.subheader(
        "📅 Choose Date"
    )

    selected_date = st.date_input(
        "Track Date",
        value=date.today(),
        max_value=date.today()
    )

    selected_date = str(selected_date)

    saved_habits = get_habits(
        USER_ID,
        selected_date
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        render_section(
            "🌅 Morning",
            MORNING_HABITS,
            selected_date,
            saved_habits
        )

        render_section(
            "💻 Productivity",
            PRODUCTIVITY_HABITS,
            selected_date,
            saved_habits
        )

    with col2:

        render_section(
            "🧠 Mental Health",
            MENTAL_HEALTH_HABITS,
            selected_date,
            saved_habits
        )

        render_section(
            "🌙 Night Reset",
            NIGHT_HABITS,
            selected_date,
            saved_habits
        )

    st.markdown("---")

    st.subheader(
        "📝 Cheat Detection"
    )

    total_habits = (
        len(MORNING_HABITS)
        + len(PRODUCTIVITY_HABITS)
        + len(MENTAL_HEALTH_HABITS)
        + len(NIGHT_HABITS)
    )

    completed = sum(
        1
        for value in saved_habits.values()
        if value == "True"
    )

    cheat_percentage = int(
        ((total_habits - completed)
        / total_habits) * 100
    )

    if cheat_percentage > 50:

        st.error(
            f"⚠️ Cheat Day Detected ({cheat_percentage}% missed)"
        )

    else:

        st.success(
            "🔥 Good consistency maintained"
        )

    st.markdown("---")

    st.subheader(
        "🎯 Main Character Goal"
    )

    st.text_input(
        "Today's Goal",
        key=f"goal-{selected_date}"
    )

    st.subheader(
        "📝 Notes"
    )

    st.text_area(
        "Daily Notes",
        key=f"notes-{selected_date}"
    )