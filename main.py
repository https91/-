import streamlit as st

# 🌟 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🌈 헤더 꾸미기
st.markdown(
    "<h1 style='text-align: center; color: #6c63ff;'>✨ MBTI로 보는 직업 추천 ✨</h1>",
    unsafe_allow_html=True
)
st.markdown("<h3 style='text-align: center;'>당신의 성격 유형에 맞는 꿈의 직업을 찾아보세요! 💖</h3>", unsafe_allow_html=True)

st.markdown("---")

# 🎨 이모지 테마 컬러
bg_color = "#f9f1ff"

# 🧠 MBTI 데이터
mbti_careers = {
    "INTJ": ["🔬 과학자", "📊 데이터 분석가", "📈 전략 컨설턴트"],
    "INFP": ["🎨 예술가", "✍️ 작가", "🧠 심리상담가"],
    "ENFP": ["🎤 마케터", "🌍 여행기획자", "🎬 크리에이터"],
    "ESTJ": ["💼 관리자", "📋 프로젝트 매니저", "🏦 금융분석가"],
    "ISTP": ["🔧 엔지니어", "🚘 자동차 정비사", "🧗 탐험가"],
    "ESFP": ["🎭 배우", "🎶 음악가", "🎉 이벤트 플래너"],
    "INFJ": ["🧘‍♀️ 상담사", "📚 교육자", "🌱 환경운동가"],
    "ENTP": ["🚀 스타트업 창업자", "🧪 발명가", "🎮 게임기획자"],
    # 원한다면 16가지 MBTI 다 넣을 수 있어!
}

# 🌟 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 😊", list(mbti_careers.keys()))

if selected_mbti:
    st.markdown(f"### 🔍 {selected_mbti} 유형에게 추천하는 직업은?")
    careers = mbti_careers[selected_mbti]
    for job in careers:
        st.markdown(f"- {job}")

    st.markdown("💬 *자신의 성격을 이해하고, 그에 맞는 직업을 탐색해보는 건 멋진 일이에요!* 💪")

# 🎨 바닥 꾸미기
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
