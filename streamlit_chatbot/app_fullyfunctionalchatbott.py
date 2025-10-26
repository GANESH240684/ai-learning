import streamlit as st

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("My first Streamlit App")
st.write("My first Streamlit window")

text = st.text_input("How may i help you?")
if st.button("send") and text:
    st.write("You said", text) 