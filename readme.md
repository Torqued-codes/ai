# 🤖 Startup Market Sentiment Analyzer

An autonomous, multi-page data pipeline designed to crawl startup directories, extract unstructured information, and derive actionable AI-driven intelligence.

## 📌 Overview
This project represents an end-to-end data pipeline. It moves beyond simple web scraping by integrating a multi-stage workflow: **Autonomous Crawling → Sentiment Intelligence → Structured Data Export**. It is built to transform raw web text into high-quality, labeled datasets suitable for AI matchmaking and predictive modeling.

## 🛠 Core Pipeline Features

- **Autonomous Crawling (Pagination Engine):** - Implements an intelligent loop that automatically traverses multi-page directory structures.
  - Dynamically detects and follows "Next" navigation links, enabling the harvesting of complete, large-scale datasets.
- **AI-Driven Sentiment Intelligence:** - Integrates `TextBlob` (NLP) to perform real-time sentiment analysis on extracted text.
  - Quantifies qualitative company data (headlines, descriptions) into structured sentiment scores (Positive, Negative, Neutral).
- **Production-Ready Architecture:** - **Decoupled Logic:** The `Scraper Engine` is independent of the `Analyzer`, allowing for rapid swapping of data sources or AI models without refactoring the core codebase.
  - **Config-Driven:** Easily adaptable to new target sites by updating a centralized configuration dictionary.
- **Robust Data Handling:** - Uses `pandas` to aggregate and clean data, exporting production-ready CSVs with full data lineage.
  - Implements custom `User-Agent` headers and error handling to ensure resilient crawling.



## 🚀 Quick Start

1. **Install Dependencies:**

   pip install requests beautifulsoup4 pandas textblob


2. **Run the Pipeline:**

    python main.py

3. **Output:**

    The processed intelligence is exported to /data/sentiment_results.csv, featuring a structured table of company titles and their corresponding sentiment scores.

## 🏗 Why this is Usefull

This project demonstrates key engineering competencies required for AI/ML roles:

- Scalability: The ability to navigate entire websites autonomously.

- NLP Application: Understanding how to integrate sentiment analysis to create "market health indicators" from raw text.

- Modular Engineering: Writing maintainable, clean code that treats data collection and data transformation as distinct, scalable services.

- Process Automation: Transforming a manual task into a fully automated, hands-off pipeline.
