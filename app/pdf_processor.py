"""PDF loading and text splitting."""

import tempfile
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


def process_pdfs(uploaded_files) -> list:
    all_chunks = []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        pages = loader.load()

        for page in pages:
            page.metadata["source"] = uploaded_file.name

        chunks = splitter.split_documents(pages)
        all_chunks.extend(chunks)

        Path(tmp_path).unlink(missing_ok=True)

    return all_chunks
