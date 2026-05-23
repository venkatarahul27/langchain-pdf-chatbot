# LangChain PDF Chatbot

Conversational AI chatbot that lets you upload PDFs and ask questions about their content. Built with LangChain, ChromaDB for vector storage, and Streamlit for the UI. Supports multi-document conversations with source citations.

## Features

- **PDF Upload & Processing** — drag-and-drop PDF upload with automatic text extraction and chunking
- **Conversational Memory** — maintains chat history for follow-up questions
- **Source Citations** — every answer includes page numbers and source excerpts
- **Multi-Document Support** — upload and query across multiple PDFs simultaneously
- **Vector Search** — semantic search using ChromaDB embeddings for accurate retrieval
- **Streaming Responses** — real-time token streaming for a responsive chat experience

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Streamlit   │────▶│  LangChain   │────▶│  Claude /       │
│  Frontend    │     │  RAG Chain   │     │  OpenAI LLM     │
└─────────────┘     └──────┬───────┘     └─────────────────┘
                           │
                    ┌──────▼───────┐
                    │  ChromaDB    │
                    │  Vector Store│
                    └──────────────┘
```

## Quick Start

```bash
# Clone the repo
git clone https://github.com/venkatarahul27/langchain-pdf-chatbot.git
cd langchain-pdf-chatbot

# Install dependencies
pip install -r requirements.txt

# Set your API key
export ANTHROPIC_API_KEY=your_key

# Launch the app
streamlit run app/main.py
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Claude 3.5 Sonnet / GPT-4 |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Embeddings | HuggingFace sentence-transformers |
| PDF Parsing | PyPDF2 |
| UI | Streamlit |
| Language | Python 3.11+ |

## Project Structure

```
langchain-pdf-chatbot/
├── app/
│   ├── main.py              # Streamlit app entry point
│   ├── pdf_processor.py     # PDF loading, splitting, embedding
│   ├── chain.py             # LangChain RAG chain setup
│   └── vector_store.py      # ChromaDB operations
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

1. **Upload** — user uploads one or more PDF files
2. **Process** — PDFs are split into chunks using RecursiveCharacterTextSplitter
3. **Embed** — chunks are embedded using sentence-transformers and stored in ChromaDB
4. **Query** — user asks a question; relevant chunks are retrieved via similarity search
5. **Answer** — LLM generates an answer grounded in the retrieved context with source citations

## License

MIT
