import streamlit as st

st.title("ToDo List")

col1, col2 = st.columns(2)

with col1:
    i = 12
    for i in range(4):
        st.info("10월" + str(i) + "일")


with col2:
    i = 16
    for i in range(4):
        st.info("10월" + str(i) + "일")
    