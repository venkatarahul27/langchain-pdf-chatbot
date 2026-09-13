# LangChain PDF Chatbot

A Streamlit RAG prototype for uploading PDFs and asking questions about their contents. Uses LangChain, local sentence-transformer embeddings, ChromaDB retrieval, and Claude to generate answers with retrieved source excerpts.

## Features

- **PDF Upload & Processing** — drag-and-drop PDF upload with automatic text extraction and chunking
- **Chat Interface** — displays messages within the Streamlit session
- **Source Excerpts** — displays retrieved passages and page metadata when source documents are returned
- **Multi-Document Support** — upload and query across multiple PDFs simultaneously
- **Vector Search** — retrieves document chunks from ChromaDB using local embeddings

## Architecture

```text
PDF upload -> PyPDFLoader -> Text chunks -> Local embeddings -> ChromaDB
                                                                  |
Question -> LangChain retrieval chain -> Claude -> Answer + source excerpts
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
| LLM | Claude via `ChatAnthropic`; model configured in `app/chain.py` |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Embeddings | HuggingFace sentence-transformers |
| PDF Parsing | LangChain `PyPDFLoader` |
| UI | Streamlit |
| Language | Python 3.11+ |

## Project Structure

```
langchain-pdf-chatbot/
├── app/
│   ├── main.py              # Streamlit app entry point
│   ├── pdf_processor.py     # PDF loading and splitting
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

## Current Limitations

- Answers render after the model call completes; token streaming is not implemented.
- The retrieval chain is recreated for each question. Follow-up conversation behavior needs dedicated testing.
- Retrieved excerpts help inspect an answer but do not guarantee its accuracy or complete citation coverage.
- The vector store persists to a shared local `./chroma_db` directory. Separate user and document collections are future work.
- Automated tests and retrieval-quality evaluations have not been added yet.

## Contributing

Improvements to session handling, retrieval evaluation, and source display are welcome. Include a small reproducible example with behavior changes.

## License

[MIT](LICENSE)
