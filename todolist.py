import streamlit as st

st.title("ToDo List")

if "todo_list" not in st.session_state:
    st.session_state.todo_list = {}

cols = st.columns(4)

for i, day in enumerate(range(12, 28)):
    with cols[i % 4]:
        date = f"10월 {day}일"

        st.info(date)

# with cols:
#     for i in range(8, 24):
#         st.info("10월 일")

#         st.success(" ")
        
#         with st.form("list_form"):
#             list = st.text_input("할 일")
#             if st.form_submit_button("등록") and list:
#                 st.session_state.todo_list.append(list)

    