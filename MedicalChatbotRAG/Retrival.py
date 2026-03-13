""" # step 1: Setup LLM
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv , find_dotenv
from langchain_community.vectorstores import FAISS
import os

load_dotenv(find_dotenv())

HF_TOKEN = os.getenv("HF_TOKEN")
huggingface_repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
def load_llm(huggingface_repo_id):
    llm = HuggingFaceEndpoint(
        repo_id=huggingface_repo_id,
        temperature=0.5,

        model_kwargs={
            "token":HF_TOKEN,
            "max_length":512
            }
    )
    return llm



# step 2: Connect LLM with FAISS
CUSTOM_PROMPT_TEMPLATE = 
#Use the pieces of information provided in the context to answer user's question.
#If you dont know the answer, just say that you dont know, dont try to make up an answer. 
#Dont provide anything out of the given context

#Context: {context}
#Question: {question}

#tart the answer directly. No small talk please.


def set_custom_prompt(custom_prompt_template):
    prompt=PromptTemplate(
        template=custom_prompt_template, 
        input_variables=["context", "question"]
        )
    return prompt

# Load Database
DB_FAISS_PATH="vectorstore/db_faiss"
embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db=FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)


# step 3: Create Chain
qa_chain=create_retrieval_chain(
    llm=load_llm(huggingface_repo_id),
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={'k':3}),
    return_source_documents=True,
    chain_type_kwargs={'prompt':set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
)

# Now invoke with a single query
user_query = input("Write Query Here: ")

response = qa_chain.invoke({"input": user_query})

print("\nRESULT:\n", response["answer"])
print("\nSOURCE DOCUMENTS:\n", response["context"])

"""

from dotenv import load_dotenv, find_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# ---------------------------
# ENV SETUP
# ---------------------------
load_dotenv(find_dotenv())
HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH = "vectorstore/db_faiss"


# ---------------------------
# LLM
# ---------------------------
llm = HuggingFaceEndpoint(
    repo_id=MODEL_ID,
    temperature=0.5,
    model_kwargs={
        "token": HF_TOKEN,
        "max_length": 512
    }
)


# ---------------------------
# PROMPT
# ---------------------------
prompt = ChatPromptTemplate.from_template("""
Use the provided context to answer the question.
If you don't know the answer, say you don't know.
Do NOT make up answers.

Context:
{context}

Question:
{question}

Answer:
""")


# ---------------------------
# VECTOR STORE
# ---------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    DB_FAISS_PATH,
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})


# ---------------------------
# LCEL RAG CHAIN (✔ CORRECT)
# ---------------------------
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)


# ---------------------------
# RUN
# ---------------------------
query = input("Write Query Here: ")
result = rag_chain.invoke(query)

print("\nRESULT:\n", result)
