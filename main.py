import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="✨MBTI 진로 추천✨",
    page_icon="💼",
    layout="centered"
)

# 스타일용 CSS (배경, 폰트, 박스 꾸미기)
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f8f0ff 0%, #d3c6ff 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #3a0ca3;
    }
    .stButton>button {
        background: #8338ec;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 20px;
        margin-top: 10px;
    }
    .job-box {
        background: #e0c3fc;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        font-size: 1.1rem;
        box-shadow: 3px 3px 8px rgba(131, 56, 236, 0.5);
    }
    .hint-box {
        background: #ffecb3;
        border-radius: 12px;
        padding: 12px;
        margin: 10px 0 20px 0;
        font-size: 1rem;
        color: #795548;
        box-shadow: 2px 2px 6px rgba(255, 193, 7, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main'>", unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align:center; font-size:3rem;'>🌈 MBTI 진로 추천 웹앱 💼</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; margin-bottom:40px;'>당신의 MBTI에 딱 맞는 꿈의 직업을 찾아보세요! 🎉</h3>", unsafe_allow_html=True)

# MBTI별 직업, 해석, 힌트 데이터
data = {
    "INTJ": {
        "jobs": ["🔬 과학자", "📊 데이터 분석가", "📈 전략 컨설턴트", "💻 소프트웨어 엔지니어"],
        "interpretation": "INTJ는 전략적이고 논리적인 계획가입니다. 독창적이고 목표 지향적이며 문제 해결을 즐깁니다.",
        "hint": "🔍 혼자 깊게 고민하는 걸 좋아하고, 체계적인 환경에서 빛나요."
    },
    "INFP": {
        "jobs": ["🎨 예술가", "✍️ 작가", "🧠 심리상담가", "🌿 환경운동가"],
        "interpretation": "INFP는 이상주의자이며, 자기 내면의 가치에 충실합니다. 감수성이 풍부하고 창의력이 뛰어납니다.",
        "hint": "💡 자기표현과 사람들의 마음을 이해하는 일을 좋아해요."
    },
    "ENFP": {
        "jobs": ["🎤 마케터", "🌍 여행기획자", "🎬 크리에이터", "🤝 인사 담당자"],
        "interpretation": "ENFP는 활기차고 사람을 좋아하는 낙천가입니다. 창의적이고 새로운 경험을 추구합니다.",
        "hint": "🔥 사람들과 어울리고, 변화를 즐기며, 아이디어가 많아요."
    },
    "ESTJ": {
        "jobs": ["💼 관리자", "📋 프로젝트 매니저", "🏦 금융분석가", "🏢 공무원"],
        "interpretation": "ESTJ는 현실적이고 책임감이 강한 리더형입니다. 조직적이고 규칙을 중시합니다.",
        "hint": "📅 계획 세우고, 일을 체계적으로 처리하는 데 능숙해요."
    },
    # ... 여기에 16가지 MBTI 모두 추가 가능 ...
}

mbti_list = list(data.keys())

# MBTI 선택
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요!", mbti_list)

if selected_mbti:
    st.markdown(f"<h2 style='text-align:center;'>✨ {selected_mbti} 유형 ✨</h2>", unsafe_allow_html=True)

    # 직업 추천 박스
    st.markdown("<h3>💼 추천 직업들</h3>", unsafe_allow_html=True)
    for job in data[selected_mbti]["jobs"]:
        st.markdown(f"<div class='job-box'>{job}</div>", unsafe_allow_html=True)

    # 해석과 힌트 토글용 버튼
    if 'show_hint' not in st.session_state:
        st.session_state.show_hint = False

    def toggle_hint():
        st.session_state.show_hint = not st.session_state.show_hint

    st.markdown("<h3>🧠 MBTI 해석</h3>", unsafe_allow_html=True)
    st.markdown(f"<p>{data[selected_mbti]['interpretation']}</p>", unsafe_allow_html=True)

    if st.button("💡 힌트 보기 / 숨기기", on_click=toggle_hint):
        pass

    if st.session_state.show_hint:
        st.markdown(f"<div class='hint-box'>{data[selected_mbti]['hint']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 하단 푸터
st.markdown("<hr>")
st.markdown("<p style='text-align:center; color:#999;'>© 2025 MBTI 진로 추천 앱 by ChatGPT 💜</p>", unsafe_allow_html=True)
