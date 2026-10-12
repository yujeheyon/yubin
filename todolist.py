import streamlit as st

st.title("ToDo List")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    for i in range(4):
        st.info("10월" + str(i + 7) + "일")
    