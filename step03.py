import streamlit as st

st.title("메인 제목")
st.info("파란색 알림 박스")
st.success("초록색 성공 메시지")

col1, col2 = st.columns(2)

# 데이터 입력
name = st.text_input("이름")
btn  = st.button("클릭")

# 폼 입력 & 상태 관리
with st.form("my_form"):
    submit = st.form_submit_button("전송")

st.session_state.login = True

# 화면 레이아웃 구성
st.title("나의 첫 웹앱")
st.info("파이썬만으로 제작하는 UI")

with col1:
    st.success("왼쪽 영역")
with col2:
    st.write("오른쪽 영역")

# 데이터 입력
name = st.text_input("이름")
btn  = st.button("다음")

# 폼 입력 & 상태 관리
with st.form("my_form"):
    submit = st.form_submit_button("전송")

st.session_state.login = True

# 화면 레이아웃 구성
st.title("나의 첫 웹앱")
st.info("파이썬만으로 제작하는 UI")

# 새로고침 시 데이터 유지
if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text_input("이름")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)

tasks = [
    
    "1. API 스펙 문서 작성",
    "2. 프론트엔드 컴포넌트 개발",
    "3. 배포 파이프라인(CI/CD) 구축"

]

st.subheader("📌금일 할 일 목록")

for task in tasks:
    with st.container(border=True):
        st.write(task)
        st.session_state.user_list.append(name)
