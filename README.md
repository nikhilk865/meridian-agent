# 🧭 Meridian Agent

> **An M365 Enterprise Knowledge Agent transforming unstructured lecture streams into interactive study hubs.**

---

## 📺 Project Demo
* [Link to 3-Minute Demo Video](https://YOUR-VIDEO-LINK-HERE)

## 💡 Problem Statement
Students and enterprise trainees spend hours scrubbing through recorded live video streams to locate specific concepts. While automated transcription exists, raw text remains unstructured, dense, and largely inaccessible to varied learning speeds or non-native speakers.

## 🚀 Our Solution
**Meridian Agent** integrates directly into Microsoft Teams using the Microsoft 365 Agents SDK. It captures live lecture feeds, processes them via Azure AI, and converts chaotic audio into a structured, queryable knowledge base.

### Key Features
* **Dynamic Knowledge Ingestion**: Automatically pipes transcripts into Azure Cosmos DB using vector embeddings.
* **On-Demand AI Class Wizard**: A native Teams chat agent that answers complex questions using multi-step reasoning.
* **Automated Study Kit**: Instantly converts raw transcripts into interactive flashcards and quizzes using Azure OpenAI (GPT-4o).
* **Universal Accessibility**: Implements real-time translation overlays using Azure AI Speech.

## 🛠️ System Architecture
1. **Frontend**: Microsoft Teams Custom App Extension (TypeScript / M365 Agents SDK)
2. **Backend**: FastAPI Gateway (Python)
3. **AI Pipeline**: Azure OpenAI Service & Azure AI Speech
4. **Database Vector Store**: Azure Cosmos DB

## ⚙️ Local Setup Instructions
1. Clone this repository: `git clone https://github.com`
2. Install Python dependencies: `pip install -r backend/requirements.txt`
3. Configure your environment variables in a local `.env` file (Do not commit this file to GitHub).
4. Run the development server: `uvicorn backend.app:app --reload`

## ⚖️ Hackathon Compliance
* **Confidentiality**: No production keys or proprietary enterprise credentials are stored in this repository. All configuration is managed via external environment variables.
* **Code of Conduct**: This repository strictly adheres to the Contributor Covenant Code of Conduct.
