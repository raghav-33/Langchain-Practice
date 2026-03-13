############# Simple Syntax of Text Loader ##################
from langchain_community.document_loaders import TextLoader

# 1. Specify your file path
file_path = "cricket.txt"

# 2. Create the TextLoader instance
loader = TextLoader(file_path , encoding='utf-8')

# 3. Load the documents
documents = loader.load()

# 4. Explore the loaded content
''' Output is always in from of list '''
print(type(documents))
print(documents[0])   # meta data + page Content
print("First document content:", documents[0].page_content)  # Page Content
print("meta data is :" , documents[0].metadata)  # meta content


###### Working of Text loader with Document ###################
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
