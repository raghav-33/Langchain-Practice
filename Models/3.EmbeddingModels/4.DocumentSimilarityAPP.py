# Document Similarity App

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# Our Pdf/Document
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# User Query / Question
query = 'tell me about bumrah'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# CAlculate Cosins Similarity Between Our Document/Pdf and User Query
scores = cosine_similarity([query_embedding], doc_embeddings)[0]    
'''
we have to pass Both Query and Document Embedding as 2d list ,
 so Query embedding pass as List , 
 Since document embedding is already list above created so not use list brackets
'''

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

'''
Enumerate the Embedding result List {that is assign a index or no according to position}
Index : Indicate Which Senetnece i.e ; 1,2,3,4...
Now Sort The list in Ascending order and fetch the last By using -1
We get Now index /position value of sentence with larger cosine similarity score

NOTE: same approach is used in RAG based application the only differnce is here we are not storing Embedding
      evry time we generating embedding which is costlty , but in RAGs we store embedding in vector databases
'''

print(query)
print(documents[index])
print("similarity score is:", score)