from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import csv
import json
from pathlib import Path
from typing import Type
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
import yfinance as yf
from crewai.tools import BaseTool
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Example input schema for all tools
class ToolInput(BaseModel):
    query: str = Field(..., description="Query or path for the tool task.")

# 1. FileReadTool: For reading local text/CSV files
class FileReadTool(BaseTool):
    name: str = "File Read Tool"
    description: str = "Reads and extracts data from local files. Use for .txt, .csv, or similar."
    args_schema: Type[BaseModel] = ToolInput

    def _run(self, query: str) -> str:
        # Implement file reading logic here
        # Example: Open and read file, return contents
        return f"Contents of file at: {query}"

# 2. PdfReadTool: For extracting data from PDF files
class PdfReadTool(BaseTool):
    name: str = "PDF Read Tool"
    description: str = "Extracts data from PDF files for financial statements, reports, etc."
    args_schema: Type[BaseModel] = ToolInput

    def _run(self, query: str) -> str:
        # Implement PDF reading logic here
        return f"Extracted data from PDF at: {query}"

# 3. ExcelReadTool: For reading Excel spreadsheets (.xls/.xlsx)
class ExcelReadTool(BaseTool):
    name: str = "Excel Read Tool"
    description: str = "Reads and processes Excel spreadsheets for financial data extraction."
    args_schema: Type[BaseModel] = ToolInput

    def _run(self, query: str) -> str:
        # Implement Excel reading logic here
        return f"Extracted data from Excel file at: {query}"

# 4. SerperDevTool: For web search (news, financial updates, etc.)
class SerperDevTool(BaseTool):
    name: str = "Serper Dev Web Search Tool"
    description: str = "Performs web search for news, market updates, and contextual financial information."
    args_schema: Type[BaseModel] = ToolInput

    def _run(self, query: str) -> str:
        # Implement web search logic here
        return f"Web search results for: {query}"

# 5. WebScraperTool: For scraping structured web data (financial sites, competitor info)
class WebScraperTool(BaseTool):
    name: str = "Web Scraper Tool"
    description: str = "Scrapes structured web data from financial portals, competitor pages, etc."
    args_schema: Type[BaseModel] = ToolInput

    def _run(self, query: str) -> str:
        # Implement web scraping logic here
        return f"Scraped web data for: {query}"


# 6. YFinanceTool: for live stock data fetching
class YFinanceTool(BaseTool):
    name: str = "yfinance_stock_data"
    description: str = "Fetches live stock data for a given ticker symbol"

    def _run(self, ticker: str) -> str:
        stock = yf.Ticker(ticker)
        info = stock.info
        return str({
            "name": info.get("longName"),
            "price": info.get("currentPrice"),
            "pe_ratio": info.get("trailingPE"),
            "market_cap": info.get("marketCap"),
            "52w_high": info.get("fiftyTwoWeekHigh"),
            "52w_low": info.get("fiftyTwoWeekLow"),
        })


# 7. 
class SentimentTool(BaseTool):
    name: str = "sentiment_analyzer"
    description: str = "Analyzes sentiment of financial news text. Input: news headline or paragraph."

    def _run(self, text: str) -> str:
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        label = "BULLISH" if scores["compound"] > 0.05 else "BEARISH" if scores["compound"] < -0.05 else "NEUTRAL"
        return f"Sentiment: {label} | Scores: {scores}"

# 8.
import urllib.request
import xml.etree.ElementTree as ET
from crewai.tools import BaseTool

class StockNewsTool(BaseTool):
    name: str = "stock_news_fetcher"
    description: str = "Fetches latest 5 news headlines for a stock ticker from Yahoo Finance RSS. Input: ticker symbol like RELIANCE.NS"

    def _run(self, ticker: str) -> str:
        url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=IN&lang=en-IN"
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                tree = ET.parse(response)
            items = tree.findall(".//item")
            headlines = [item.find("title").text for item in items[:5]]
            return "\n".join(headlines) if headlines else "No headlines found."
        except Exception as e:
            return f"Error fetching news: {str(e)}"