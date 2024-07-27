import streamlit as st
import random

st.set_page_config(page_title="Aceitas?", page_icon=":heart:", layout="centered")

st.markdown("<h1 style='text-align: center; color: #590d22;'>Quer vir aqui jogar comigo?</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if 'button_clicked' not in st.session_state:
        st.session_state['button_clicked'] = False

    def move_button_1():
        st.session_state['button_clicked'] = not st.session_state['button_clicked']

    if st.session_state['button_clicked']:
        st.warning("Não")
        x, y = random.randint(0, 100), random.randint(0, 100)
        st.button("Não", key="move_button", on_click=move_button_1)
    else:
        st.button("Não", key="move_button", on_click=move_button_1)

    if st.button("Sim"):
        st.success("Fico bem feliz com você ter aceitado, HIHIHIHI, bora ouvir H&J?")


