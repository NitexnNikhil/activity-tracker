import streamlit as st
import random

quotes = [

    "Discipline creates freedom.",

    "Your future is watching you.",

    "Small habits build big results.",

    "You become what you repeat daily.",

    "Consistency beats motivation."
]

def render_quote():

    quote = random.choice(quotes)

    st.markdown(
        f'''
        <div style="
            padding:20px;
            border-radius:20px;
            background:rgba(255,255,255,0.08);
            text-align:center;
            font-size:22px;
        ">
            ✨ {quote}
        </div>
        ''',
        unsafe_allow_html=True
    )