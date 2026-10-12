import streamlit as st

st.title("ToDo List")

if "todo_list" not in st.session_state:
        st.session_state.todo_list = []

col1, col2, col3, col4= st.columns(4)

with col1:
    st.info("10월 12일")

    with st.form("todo_form_12"):
        todo = st.text_input("할 일", key="todo_12")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 16일")

    with st.form("todo_form_16"):
        todo = st.text_input("할 일", key="todo_16")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 20일")

    with st.form("todo_form_20"):
        todo = st.text_input("할 일", key="todo_20")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 24일")

    with st.form("todo_form_24"):
        todo = st.text_input("할 일", key="todo_24")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

with col2:
    st.info("10월 13일")

    with st.form("todo_form_13"):
        todo = st.text_input("할 일", key="todo_13")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 17일")

    with st.form("todo_form_17"):
        todo = st.text_input("할 일", key="todo_17")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 21일")

    with st.form("todo_form_21"):
        todo = st.text_input("할 일", key="todo_21")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 25일")

    with st.form("todo_form_25"):
        todo = st.text_input("할 일", key="todo_25")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

with col3:
    st.info("10월 14일")

    with st.form("todo_form_14"):
        todo = st.text_input("할 일", key="todo_14")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 18일")

    with st.form("todo_form_18"):
        todo = st.text_input("할 일", key="todo_18")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 22일")

    with st.form("todo_form_22"):
        todo = st.text_input("할 일", key="todo_22")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 26일")

    with st.form("todo_form_26"):
        todo = st.text_input("할 일", key="todo_26")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

with col4:
    st.info("10월 15일")

    with st.form("todo_form_15"):
        todo = st.text_input("할 일", key="todo_15")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 19일")

    with st.form("todo_form_19"):
        todo = st.text_input("할 일", key="todo_19")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 23일")

    with st.form("todo_form_23"):
        todo = st.text_input("할 일", key="todo_23")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)

    st.info("10월 27일")

    with st.form("todo_form_27"):
        todo = st.text_input("할 일", key="todo_27")
        btn  = st.form_submit_button("등록")

        if btn and todo:
            st.session_state.todo_list.append(todo)

    for item in st.session_state.todo_list:
        st.success(item)
    