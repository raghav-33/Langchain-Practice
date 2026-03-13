# Model import
from langchain_openai import OpenAIEmbeddings

# Dotenv import for Api key calling
from dotenv import load_dotenv
load_dotenv()

# Model or Object Created
embedding = OpenAIEmbeddings(model="text-embedding-3large",dimensions=32)
''' Greater Vector Dimension capture greater Context and viceversa'''

# Model Calling
result = embedding.embed_query("Delhi is the capital of India")

# print Embeddings
''' Note: Before prininting convert it into {String} , so it can see correctly '''
print(str(result))



