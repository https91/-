import streamlit as st
import random

# 🌟 페이지 설정
st.set_page_config(
    page_title="MBTI 이모지 추측 게임",
    page_icon="🧠",
    layout="centered"
)

# 🌈 제목
st.markdown("<h1 style='text-align:center; color:#ff69b4;'>🧠 MBTI 이모지 추측 게임 🎯</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>이 이모지들은 어떤 MBTI를 나타낼까요? 맞춰보세요! 😊</h4>", unsafe_allow_html=True)

st.markdown("---")

# 🎯 MBTI별 이모지 힌트 정의
mbti_emoji = {
    "INTJ": "🧠📚🧊📈",
    "INFP": "🌈📖🎨🌙",
    "ENFP": "🎉🌟🗣️🎨",
    "ISTJ": "📋🕰️🔍🏛️",
    "ESTP": "🏎️🔥🎯🎲",
    "INFJ": "🌌🕊️🧘‍♂️📚",
    "ENTP": "💡🤹‍♂️🧪🔥",
    "ESFJ": "🤝🍰📅💐",
    "ISFP": "🎨🌿🎵😌",
    "ESTJ": "📈📊🗂️🏆",
    "ISFJ": "👩‍⚕️📦🎁🛏️",
    "ENTJ": "🚀📣📊🧠",
    "INTP": "🔬🧩🤖📚",
    "ENFJ": "📣💖📘🧑‍🤝‍🧑",
    "ESFP": "🎤💃🌟🍹",
    "ISTP": "🔧⚙️🧭🏍️"
}

# 🔁 게임용 MBTI 랜덤 선택
if 'answer' not in st.session_state:
    st.session_state.answer = random.choice(list(mbti_emoji.keys()))

# 👁️ 이모지 힌트 출력
current_emoji = mbti_emoji[st.session_state.answer]
st.markdown(f"## 🤔 이 MBTI는 누구일까요?\n### {current_emoji}")

# 🎯 사용자 선택
guess = st.selectbox("👇 정답이라고 생각하는 MBTI를 선택하세요:", list(mbti_emoji.keys()))

# ✅ 정답 확인
if st.button("정답 확인하기!"):
    if guess == st.session_state.answer:
        st.success(f"🎉 정답입니다! {guess}는 {current_emoji}와 잘 어울려요!")
    else:
        st.error(f"😢 아쉽네요! 정답은 {st.session_state.answer}였습니다.")
    st.balloons()

# 🔄 다시하기
if st.button("🔄 새로운 문제로 다시하기"):
    st.session_state.answer = random.choice(list(mbti_emoji.keys()))
    st.experimental_rerun()

# 👣 바닥
st.markdown("---")
st.markdown("<p style='text-align:center; color:#aaa;'>© 2025 MBTI Emoji Game by Streamlit</p>", unsafe_allow_html=True)

