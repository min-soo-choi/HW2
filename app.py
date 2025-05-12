import streamlit as st

st.title("📝 HW2 streamlit with AWS 퀴즈")

# 객관식 문제
st.header("1. 객관식 문제")
st.write("5/12 까지 오픈소스소프트웨어 강의에서 진행되지 않은 강의를 고르시오.")
mc_answer = st.radio(
    "보기 중에서 하나를 선택하세요.",
    ("Streamlit", "linux", "github", "HuggingFace")
)

# 주관식 문제
st.header("2. 주관식 문제")
st.write("오픈소스소프트웨어 강의는 몇학년 전공 선택 강의인가요?")
subjective_answer = st.text_input("정답을 입력하세요.")

# 제출 버튼
if st.button("제출"):
    # 정답 체크
    mc_correct = mc_answer == "HuggingFace"
    subjective_correct = subjective_answer.strip().lower() == "2학년"

    # 결과 출력
    st.subheader("결과")
    st.write(f"객관식: {'✅ 정답' if mc_correct else '❌ 오답'}")
    st.write(f"주관식: {'✅ 정답' if subjective_correct else '❌ 오답'}")
