import streamlit as st

st.title("ToDo List")

col1, col2, col3, col4= st.columns(4)

with col1:
    for i in range(4):
        st.info("10월" + str(i + 1) + "일")

with col2:
    for i in range(4):
        st.info("10월" + str(i + 1) + "일")

with col3:
    for i in range(4):
        st.info("10월" + str(i + 1) + "일")

with col4:
    for i in range(4):
        st.info("10월" + str(i + 1) + "일")
    