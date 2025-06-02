import streamlit as st
import random

# --- 페이지 세팅 ---
st.set_page_config(
    page_title="MBTI 이모지 추측 게임",
    page_icon="🎯",
    layout="centered"
)

# --- MBTI 데이터 정의 ---
mbti_data = {
    "INTJ": {
        "emoji": "🧠📚📈🧊",
        "interpretation": "논리적이고 전략적인 완벽주의자. 독창적이며 분석에 강합니다.",
        "hint": "혼자 조용히 생각하며 미래를 계획하는 걸 좋아해요."
    },
    "INFP": {
        "emoji": "🌈📖🎨🌙",
        "interpretation": "감수성 풍부한 이상주의자. 상상력과 창의력이 넘칩니다.",
        "hint": "자기만의 세계와 가치관을 중요하게 여겨요."
    },
    "ENFP": {
        "emoji": "🎉🌟🗣️🎬",
        "interpretation": "에너지 넘치고 사람을 사랑하는 자유로운 영혼!",
        "hint": "새로운 사람, 새로운 아이디어를 좋아하고 말이 많아요."
    },
    "ISTJ": {
        "emoji": "📋🧱🕰️📏",
        "interpretation": "신뢰감 있고 책임감 강한 관리자형. 계획과 질서를 좋아합니다.",
        "hint": "규칙을 지키고, 실용적인 걸 선호해요."
    },
    "ESFP": {
        "emoji": "🎤💃🍹🎉",
        "interpretation": "무대 위의 스타! 사교적이고 감각적인 분위기 메이커입니다.",
        "hint": "사람들과 즐겁게 노는 걸 좋아하고, 지금 이 순간에 집중해요."
    }
    # 원한다면 16개 다 추가 가능
}

mbti_list = list(mbti_data.keys())

# --- 세션 상태 초기화 ---
if "answer" not in st.session_state:
    st.session_state.answer = random.choice(mbti_list)
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# --- 제목 및 설명 ---
st.markdown("<h1 style='text-align:center;'>🧠 MBTI 이모지 추측 게임</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>이모지로 표현된 성격을 보고 어떤 MBTI인지 맞춰보세요!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- 이모지 보여주기 ---
st.markdown(f
