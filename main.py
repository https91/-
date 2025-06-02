import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🧠 MBTI 이모지 추측 게임",
    page_icon="🎲",
    layout="centered"
)

# 스타일링
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #03045e;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
    }
    .emoji-box {
        font-size: 4rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .hint-box {
        background: #fffbcc;
        padding: 15px;
        border-radius: 10px;
        margin-top: 1rem;
        box-shadow: 3px 3px 7px rgba(255, 193, 7, 0.5);
        color: #665500;
    }
    button {
        background-color: #0077b6 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 10px 25px !important;
        margin-top: 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>🧠 MBTI 이모지 추측 게임 🎯</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>주어진 이모지를 보고 어떤 MBTI인지 맞춰보세요!</p>", unsafe_allow_html=True)
st.markdown("---")

# MBTI별 이모지 특징, 해석, 힌트
mbti_data = {
    "INTJ": {
        "emoji": "🧠📚🧊📈",
        "interpretation": "논리적이고 전략적인 계획자입니다. 독창적이고 목표 지향적입니다.",
        "hint": "혼자 조용히 집중하는 걸 좋아하고, 복잡한 문제 해결에 강해요."
    },
    "INFP": {
        "emoji": "🌈📖🎨🌙",
        "interpretation": "이상주의자이며 감성적입니다. 자기 내면의 가치에 충실합니다.",
        "hint": "감수성이 풍부하고 창의적인 표현을 좋아해요."
    },
    "ENFP": {
        "emoji": "🎉🌟🗣️🎨",
        "interpretation": "활기차고 낙천적인 사람으로, 사람들과 어울리기를 좋아합니다.",
        "hint": "새로운 경험과 아이디어를 즐기며 에너지가 넘쳐요."
    },
    "ESTJ": {
        "emoji": "📋🕰️🔍🏛️",
        "interpretation": "책임감 강한 리더형으로, 조직적이고 체계적인 성격입니다.",
        "hint": "계획 세우고 규칙을 따르는 걸 중요하게 생각해요."
    }
    # 필요하면 더 추가 가능
}

mbti_keys = list(mbti_data.keys())

# 랜덤 문제 출제
if 'current_mbti' not in st.session_state:
    st.session_state.current_mbti = random.choice(mbti_keys)
    st.session_state.show_hint = False

# 이모지 문제 보여주기
st.markdown("<div class='emoji-box'>" + mbti_data[st.session_state.current_mbti]["emoji"] + "</div>", unsafe_allow_html=True)

# 사용자 선택
user_guess = st.selectbox("👇 당신이 생각하는 MBTI를 선택하세요:", mbti_keys)

# 정답 확인 버튼
if st.button("🔍 정답 확인하기!"):
    if user_guess == st.session_state.current_mbti:
        st.success(f"🎉 정답입니다! {user_guess}!")
        st.markdown(f"🧠 **해석:** {mbti_data[user_guess]['interpretation']}")
    else:
        st.error(f"😢 틀렸어요. 정답은 {st.session_state.current_mbti}였습니다.")
        st.markdown(f"🧠 **해석:** {mbti_data[st.session_state.current_mbti]['interpretation']}")

# 힌트 토글 버튼
if st.button("💡 힌트 보기 / 숨기기"):
    st.session_state.show_hint = not st.session_state.show_hint

if st.session_state.show_hint:
    st.markdown(f"<div class='hint-box'>💡 힌트: {mbti_data[st.session_state.current_mbti]['hint']}</div>", unsafe_allow_html=True)

# 문제 다시 내기 버튼
if st.button("🔄 새로운 문제 출제"):
    st.session_state.current_mbti = random.choice(mbti_keys)
    st.session_state.show_hint = False
    st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:#555;'>© 2025 MBTI 이모지 추측 게임 by ChatGPT 💙</p>", unsafe_allow_html=True)
