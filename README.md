# Codification System with LLM Embeddings and Qdrant
This project implements a semantic codification system leveraging large language model (LLM) embeddings and Qdrant vector search. It includes a FastAPI backend, a React frontend, and a Qdrant-based vector database, all optimized for French-language processing.

## 🧠 Overview
The system is designed to:

Encode input text using a French-language LLM model.

Search for semantically similar entries in a Qdrant vector database.

Serve predictions via a FastAPI REST API.

Provide a user-friendly interface through a React web application.

## 🚀 Features
LLM Embedding: Utilizes the dangvantuan/sentence-camembert-large model for French text embeddings.

Vector Search: Employs Qdrant for efficient similarity search.

FastAPI Backend: Exposes endpoints for adding data and performing searches.

React Frontend: Offers an interactive UI for users to input queries and view results.

## 🧩 Project Structure

```pgsql
codify-project/
├── backend/                 ← FastAPI + Qdrant + CamemBERT
│   ├── app/
│   │   ├── main.py
│   │   └── model.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                ← React UI
│   ├── src/
│   │   └── App.js
│   ├── public/index.html
│   └── package.json
├── docker-compose.yml       ← Orchestrates API, Qdrant, and UI
└── README.md
```
## 📦 Requirements
Python 3.8+

Node.js 14+

Docker (optional, for containerized deployment)

## 🛠️ Installation
Backend
Navigate to the backend directory.

### Install dependencies:

```bash
pip install -r requirements.txt
```
Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

### Frontend
Navigate to the frontend directory.

Install dependencies:

```bash
npm install
```

### Start the React development server:

```bash
npm start
```

### Docker (Optional)
To run the entire system using Docker:

Build the Docker images:

```bash
docker-compose build
```
Start the services:

```bash
docker-compose up
```

The application will be accessible at http://localhost:3000.

### 🔧 Usage

Add Data: Use the FastAPI endpoint /add/ to insert new items into the vector database.

Search: Use the /search/ endpoint to query the database for semantically similar items.

Frontend: Interact with the system through the React UI at the provided URL.

### 🧪 Testing

To run tests:

```bash
pytest
```

### 📢 Acknowledgments
Qdrant for the vector search engine.

Sentence-Transformers for the embedding model.

FastAPI for the backend framework.

React for the frontend framework.

