## Chat Template : for Creating Dynamic Messages ( Dynamic System , Human Messages)
''' NOTE : we have see previusly how to create dyamic prompt , now see how to create dynamic messgaes'''
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)