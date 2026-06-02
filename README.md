# 🔱 Trinetra-FinAI 
Multi-Agent AI System for Intelligent Stock Market Research & Decision Support

📌 What is Trinetra-FinAI?
Trinetra-FinAI is a multi-agent financial intelligence system built with CrewAI. It simulates a collaborative team of AI agents that work together to research, analyze, and generate a comprehensive investment report for any publicly listed company - all running 100% locally via Ollama.

## Agents & Tasks

| Agent | Role | Tasks |
|---|---|---|
| 🔍 Data Extractor | Pulls price, volume, financial statements | Data fetch, preprocessing |
| 📊 Fundamental Analyst | P/E, EPS, revenue growth, debt ratios | Fundamental scoring |
| 📈 Technical Analyst | RSI, MACD, moving averages, support/resistance | Technical signal generation |
| 📰 Sentiment Analyst | News headlines, social signals, market mood | Sentiment scoring via VADER |
| 📝 Report Writer | Synthesizes all inputs into a structured report | Final report generation |

The system follows a sequential pipeline across 5 agents and 8 tasks - from raw data extraction to final strategic report writing.
