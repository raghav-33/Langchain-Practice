from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Nodel Object Created
model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)
'''
max_completion_tokens=10 : indicate maximum no of tokens an LLM generated as output
max_completion_tokens=10 in LangChain sets a hard limit of 10 tokens for the LLM's generated response
'''

# Model calling
result = model.invoke("Write a 5 line poem on cricket")

print(result.content)