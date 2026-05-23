"""LangChain PDF Chatbot — Streamlit UI."""

import streamlit as st

from pdf_processor import process_pdfs
from chain import create_qa_chain
from vector_store import get_or_create_store

st.set_page_config(page_title="PDF Chatbot", page_icon="📄", layout="wide")
st.title("📄 PDF Chatbot")
st.caption("Upload PDFs and ask questions about their content")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader(
        "Drop your PDFs here",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if uploaded_files and st.button("Process Documents"):
        with st.spinner("Processing PDFs..."):
            chunks = process_pdfs(uploaded_files)
            st.session_state.vector_store = get_or_create_store(chunks)
            st.success(f"Processed {len(uploaded_files)} file(s) — {len(chunks)} chunks indexed")

    st.divider()
    st.markdown("**How to use:**")
    st.markdown("1. Upload one or more PDFs\n2. Click 'Process Documents'\n3. Ask questions in the chat")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question about your documents"):
    if not st.session_state.vector_store:
        st.error("Please upload and process documents first.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            chain = create_qa_chain(st.session_state.vector_store)
            response = chain.invoke({
                "question": prompt,
                "chat_history": [
                    (m["role"], m["content"]) for m in st.session_state.messages[:-1]
                ],
            })

            answer = response["answer"]
            sources = response.get("source_documents", [])

            st.markdown(answer)

            if sources:
                with st.expander("📚 Sources"):
                    for i, doc in enumerate(sources, 1):
                        page = doc.metadata.get("page", "?")
                        st.markdown(f"**Source {i}** (Page {page})")
                        st.caption(doc.page_content[:200] + "...")

        st.session_state.messages.append({"role": "assistant", "content": answer})
