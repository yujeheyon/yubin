import streamlit as st

st.title("ToDo List")

col1, col2, col3, col4= st.columns(4)

with col1:
    for i in range(8, 24):
        st.info("10월 " + str(i + 4) + "일")
        if "todo_list" not in st.session_state:
            st.session_state.todo_list = []

        st.success(" ")
        
    with st.form("list_form"):
        list = st.text_input("할 일")
        if st.form_submit_button("등록") and list:
            st.session_state.todo_list.append(list)

with col2:
    st.info("10월 13일")
    if "todo_list" not in st.session_state:
        st.session_state.todo_list = []

    st.success(" ")
    
    with st.form("list_form"):
        list = st.text_input("할 일")
        if st.form_submit_button("등록") and list:
            st.session_state.todo_list.append(list)
    st.info("10월 17일")
    st.info("10월 21일")
    st.info("10월 25일")

with col3:
    st.info("10월 14일")
    if "todo_list" not in st.session_state:
        st.session_state.todo_list = []

    st.success(" ")
    
    with st.form("list_form"):
        list = st.text_input("할 일")
        if st.form_submit_button("등록") and list:
            st.session_state.todo_list.append(list)
    st.info("10월 18일")
    st.info("10월 22일")
    st.info("10월 26일")

with col4:
    st.info("10월 15일")
    if "todo_list" not in st.session_state:
        st.session_state.todo_list = []

    st.success(" ")
    
    with st.form("list_form"):
        list = st.text_input("할 일")
        if st.form_submit_button("등록") and list:
            st.session_state.todo_list.append(list)
    st.info("10월 19일")
    st.info("10월 23일")
    st.info("10월 27일")
    