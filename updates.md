need this code base updated with new CrewAI framework

Recent updates in the CrewAI framework have focused on making multi-agent systems more production-ready and scalable. One of the major additions is Flows, which provide structured and event-driven workflow orchestration alongside traditional Crews, allowing developers to combine autonomous agent collaboration with controlled execution logic. CrewAI has also improved memory management, agent reasoning, knowledge integration (Agentic RAG), and task guardrails for more reliable outputs. New tooling such as workflow tracing, visual builders, and integrated tool support has made it easier to build, monitor, and deploy complex AI agent ecosystems efficiently.

## v0.2.0 - 2025-05-23
- Added custom YFinanceTool for live stock price and fundamentals
- Integrated into comprehensive_financial_data_analyst agent

# Changelog — Trinetra-FinAI

## v0.4.0 - 2025-05-25
- Added StockNewsTool for Yahoo Finance RSS headlines
- Wired StockNewsTool into financial health change analyst agent
- Added tools/__init__.py for clean imports

## v0.3.0 - 2025-05-24
- Added VADER-based SentimentTool for financial news analysis
- Added market_sentiment_analyst agent with SentimentTool
- Added market_sentiment_analysis task

## v0.2.0 - 2025-05-23
- Added custom YFinanceTool for live stock price and fundamentals
- Integrated YFinanceTool into financial data analyst agent

## v0.1.0 - 2025-05-22
- Added .gitignore for Python and CrewAI artifacts
- Added requirements.txt with core dependencies
- Added proper README with setup, agents overview, and usage