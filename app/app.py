import streamlit as st
import utils

st.set_page_config(page_title="EditMate",
                        page_icon="✔️",
                        layout="wide")

st.markdown("<h1 style='text-align: center;'>✍🏽 EditMate ✔️</h1>", unsafe_allow_html=True)


txt_col, corrected_txt_col = st.columns(2)

with txt_col:
    txt = st.text_area(
                    "Enter Your Text", height=300
                )

correct_me_button = st.button('Correct Text' )

if correct_me_button and txt:
    response=utils.get_response(txt)

    with corrected_txt_col:
        txt = st.text_area(
                    "Corrected Text ✔️",
                    response, height=300
                    )
if not txt:

    with corrected_txt_col:
        txt = st.text_area(
                    "Corrected Text ❗",
                    "No Text Found, Enter your text ❗", height=300
                    )
