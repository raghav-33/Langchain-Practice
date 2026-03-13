import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser


# ---------------------------------------------------
# ENV
# ---------------------------------------------------
load_dotenv()


# ---------------------------------------------------
# PDF TEXT EXTRACTION
# ---------------------------------------------------
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


# ---------------------------------------------------
# TEXT CHUNKING
# ---------------------------------------------------
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=100
    )
    return splitter.split_text(text)


# ---------------------------------------------------
# VECTOR STORE
# ---------------------------------------------------
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_texts(text_chunks, embeddings)

# ---------------------------------------------------
# FORMAT DOCUMENTS (CRITICAL FIX)
# ---------------------------------------------------
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# ---------------------------------------------------
# LLM
# ---------------------------------------------------
def get_llm():
    llm = HuggingFaceEndpoint(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="text-generation",
        temperature=0.4,
        max_new_tokens=512
    )
    return ChatHuggingFace(llm=llm)



# ---------------------------------------------------
# RAG CHAIN (SAFE VERSION)
# ---------------------------------------------------
def get_rag_chain(vectorstore):

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "fetch_k": 20}
    )

    prompt = PromptTemplate(
        template="""
You are a strict question-answering assistant from multiple pdfs uploads in app .

Rules:
- Use ONLY the provided context in pdfs
- If the answer is not present, say exactly:
  "Answer not found in the documents."
  Quote or paraphrase directly from the context
- Do NOT use outside knowledge
- Do NOT hallucinate or add external knowledge

Context:
{context}

Question:
{question}

Answer:
""",
        input_variables=["context", "question"]
    )

    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
        | prompt
        | get_llm()
        | StrOutputParser()
    )

    return chain


# ---------------------------------------------------
# STREAMLIT APP
# ---------------------------------------------------
def main():
    st.set_page_config(page_title="Chat with PDFs", page_icon="📚")
    st.header("📚 Chat with Multiple PDFs")

    user_question = st.text_input("Ask a question about your documents")

    with st.sidebar:
        st.subheader("📂 Upload PDFs")
        pdf_docs = st.file_uploader(
            "Upload PDFs and click Process",
            accept_multiple_files=True,
            type=["pdf"]
        )

        if st.button("Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF.")
            else:
                with st.spinner("Processing PDFs..."):
                    raw_text = get_pdf_text(pdf_docs)
                    chunks = get_text_chunks(raw_text)
                    st.session_state.vectorstore = get_vectorstore(chunks)
                    st.success("PDFs processed successfully!")

    if user_question:
        if "vectorstore" not in st.session_state:
            st.warning("Please process PDFs first.")
        else:
            rag_chain = get_rag_chain(st.session_state.vectorstore)

            with st.spinner("Generating answer..."):
                response = rag_chain.invoke(user_question)

            st.subheader("📌 Answer")
            st.write(response)


if __name__ == "__main__":
    main()
