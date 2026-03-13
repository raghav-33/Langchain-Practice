import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os


load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")


# Step 1: Data Ingestion

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Step 2: Text Splittings
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


# Step 3 and 4 : Embedding generation and store in vector Db
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vectorstore = FAISS.from_texts(texts=text_chunks,embedding=embeddings)
    return vectorstore


 # -----------------------------
# Step 5: Retrival
# -----------------------------
def get_retriever(vectorstore, k: int = 3):
    return vectorstore.as_retriever(
        search_kwargs={"k": k}
    )



 # -----------------------------
# Step 6: LLM Setup (HF)
# -----------------------------
def get_llm():
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.3",
        task="text-generation",
        model_kwargs={
            "temperature": 0.4,
            "max_new_tokens": 512
        }
    )
    return ChatHuggingFace(llm=llm)

 # -----------------------------
# Step 7: Chain
# -----------------------------
def get_rag_chain(retriever):
    prompt = PromptTemplate(
        template="""
       You are a helpful assistant.
       Answer the question using ONLY the context below.
       If the answer is not present, say:
      "Answer not found in the documents."

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
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | get_llm()
        | StrOutputParser()
    )

    return chain











def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")
    

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
    
    if st.button('Process'):
        with st.spinner("Processing"):
            # Get Pdf text
            raw_text = get_pdf_text(pdf_docs)

            # Get text chunk
            text_chunks = get_text_chunks(raw_text)
            st.write(text_chunks)

            # Get vector Store
            vectorstore = get_vectorstore(text_chunks)

            st.session_state.vectorstore = vectorstore
            st.success("PDFs processed successfully!")

    
    if user_question:
        if "vectorstore" not in st.session_state:
            st.warning("Please process PDFs first.")
        else:
            qa_chain = get_rag_chain(st.session_state.vectorstore)

            with st.spinner("Generating answer..."):
                response = qa_chain.invoke({"query": user_question})

            st.subheader("📌 Answer")
            st.write(response["result"])





if __name__ == "__main__":
    main()
