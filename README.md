# GenAI Financial Recommendation Engine

## Overview
[cite_start]This project is an advanced AI system built to tackle a massive problem: standard LLMs often lack real-time financial data or hallucinate numbers, which is dangerous in finance[cite: 3]. [cite_start]By combining Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) and ChromaDB, this engine essentially gives the AI a "textbook and calculator" so it can look up real facts before answering[cite: 4].

## The Core Architecture
This engine is built on three foundational pillars:
* [cite_start]**The Brain (LLM):** The language model responsible for understanding user queries and structuring financial advice[cite: 89].
* [cite_start]**The Memory (ChromaDB):** A specialized vector database that stores financial documents as numerical embeddings, making semantic meaning-based searches possible[cite: 90].
* [cite_start]**The Bridge (RAG):** The mechanism that pulls relevant information from ChromaDB and feeds it directly to the LLM to provide accurate context for its answers[cite: 91].

## The Data Pipeline
* [cite_start]**Data Ingestion:** Collecting and feeding diverse financial data, such as stock reports and banking rules, into the system[cite: 50].
* [cite_start]**Chunking & Embedding:** Breaking long documents into manageable paragraphs and converting them into mathematical vectors[cite: 51].
* [cite_start]**Storage:** Saving these resulting vectors permanently within ChromaDB[cite: 52].

## Installation & Setup
Follow these steps to initialize the environment and run the project locally.

1. Clone the repository and navigate to the project folder.
2. Create and activate a Python virtual environment.
3. [cite_start]Install the core dependencies by running: `pip install langchain chromadb python-dotenv`[cite: 133].
4. [cite_start]Create a `.env` file in the main project folder to securely hold your secret keys[cite: 136].
5. [cite_start]Add `.env` to your `.gitignore` file to ensure your secrets are never uploaded[cite: 137].

## Future Roadmap
* Transition from a static RAG application to an Agentic AI system.
* [cite_start]Convert the ChromaDB pipeline into a standalone Tool[cite: 59].
* [cite_start]Deploy the application using an intuitive UI and a cloud hosting platform[cite: 117].