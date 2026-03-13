# integration pacakge b/w langchain and openai
from langchain_openai import OpenAI

# Dotenv pacakge help to load  secret key from envoirment file 
from dotenv import load_dotenv
load_dotenv()

# object created of openai
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Calling openai model
result = llm.invoke("What is capital of india")
print(result)