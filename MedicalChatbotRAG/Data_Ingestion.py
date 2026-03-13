from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1 : Load raw Pdfs
DATA_PAth ="data/"
def load_pdf_files(data):
    loader = DirectoryLoader(
        path=data,
        glob = "*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents

documents1=load_pdf_files(data=DATA_PAth)
print("length of documents :" , len(documents1))

# Step 2: Create Chunks
def create_chunks(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

text_chunks1 =create_chunks(extracted_data=documents1)
print(len(text_chunks1))

# Step 3: Create Vector Embeddings
def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

embedding_model = get_embedding_model()


# Step 4: Store Embeddings in Vector Db 
DB_FAISS_PATH = "vectorstore/db_faiss"
db = FAISS.from_documents (text_chunks1 , embedding_model)
db.save_local(DB_FAISS_PATH)
