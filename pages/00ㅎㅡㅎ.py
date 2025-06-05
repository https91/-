# stock_top10_app.py

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 시가총액 기준 글로벌 TOP10 기업 (2025년 기준으로 자주 바뀔 수 있음)
# 이 예시는 대략적인 목록이며 필요에 따라 업데이트 가능
top10_tickers = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'NVIDIA': 'NVDA',
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Meta': 'META',
    'Berkshire Hathaway': 'BRK-B',
    'TSMC': 'TSM',
    'Eli Lilly': 'LLY',
    'Tesla': 'TSLA'
}

st.title("📈 글로벌 시가총액 TOP10 기업의 최근 1년 주가 변화")

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# yfinance로 데이터 다운로드
@st.cache_data
def load_data(tickers, start, end):
    data = {}
    for name, symbol in tickers.items():
        stock_data = yf.download(symbol, start=start, end=end)
        data[name] = stock_data['Adj Close']
    return data

with st.spinner("데이터 로딩 중..."):
    stock_prices = load_data(top10_tickers, start_date, end_date)

# Plotly 시각화
fig = go.Figure()

for company, price_series in stock_prices.items():
    fig.add_trace(go.Scatter(
        x=price_series.index,
        y=price_series.values,
        mode='lines',
        name=company
    ))

fig.update_layout(
    title="최근 1년간 주가 추이 (시가총액 TOP10 기업)",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_white",
    legend=dict(orientation="h", y=-0.2)
)

st.plotly_chart(fig, use_container_width=True)
