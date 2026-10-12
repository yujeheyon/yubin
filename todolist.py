import streamlit as st

st.title("ToDo List")

if "todo_list" not in st.session_state:
        st.session_state.todo_list = []

col1, col2, col3, col4= st.columns(4)

with col1:
    st.info("10월 12일")
    st.success(" ")

    with st.form("todo_form_12"):
        todo = st.text_input("할 일", key="todo_12")
        btn  = st.form_submit_button("등록")

    st.info("10월 16일")
    st.success(" ")

    with st.form("todo_form_16"):
        todo = st.text_input("할 일", key="todo_16")
        btn  = st.form_submit_button("등록")
    

    st.info("10월 20일")
    st.success(" ")

    with st.form("todo_form_20"):
        todo = st.text_input("할 일", key="todo_20")
        btn  = st.form_submit_button("등록")
    

    st.info("10월 24일")
    st.success(" ")

    with st.form("todo_form_24"):
        todo = st.text_input("할 일", key="todo_24")
        btn  = st.form_submit_button("등록")
    

with col2:
    st.info("10월 13일")
    st.info("10월 17일")
    st.info("10월 21일")
    st.info("10월 25일")

with col3:
    st.info("10월 14일")
    st.info("10월 18일")
    st.info("10월 22일")
    st.info("10월 26일")

with col4:
    st.info("10월 15일")
    st.info("10월 19일")
    st.info("10월 23일")
    st.info("10월 27일")
    