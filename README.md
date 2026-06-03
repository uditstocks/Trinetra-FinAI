# 🔱 Trinetra-FinAI
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![CrewAI](https://img.shields.io/badge/Framework-CrewAI-orange.svg)
![Ollama](https://img.shields.io/badge/Local_LLM-Ollama-black.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Multi-Agent AI System for Intelligent Stock Market Research & Decision Support

📌 What is Trinetra-FinAI?
Trinetra-FinAI is a multi-agent financial intelligence system built with CrewAI. It simulates a collaborative team of AI agents that work together to research, analyze, and generate a comprehensive investment report for any publicly listed company - all running 100% locally via Ollama.
## 🛠️ Built With
* **[CrewAI](https://www.crewai.com/):** For orchestrating the multi-agent framework.
* **[Ollama](https://ollama.ai/):** To run the LLMs 100% locally for privacy and zero API costs.
* **Python 3:** The core language powering the data extraction and logic.

## Agents & Tasks

| Agent | Role | Tasks |
|---|---|---|
| 🔍 Data Extractor | Pulls price, volume, financial statements | Data fetch, preprocessing |
| 📊 Fundamental Analyst | P/E, EPS, revenue growth, debt ratios | Fundamental scoring |
| 📈 Technical Analyst | RSI, MACD, moving averages, support/resistance | Technical signal generation |
| 📰 Sentiment Analyst | News headlines, social signals, market mood | Sentiment scoring via VADER |
| 📝 Report Writer | Synthesizes all inputs into a structured report | Final report generation |

The system follows a sequential pipeline across 5 agents and 8 tasks - from raw data extraction to final strategic report writing.
