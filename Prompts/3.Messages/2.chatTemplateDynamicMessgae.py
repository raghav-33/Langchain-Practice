'''
Like Prompts We have 2 type of Messages (i) Static -> (simple see in messages.py) (ii) DynamicMessages -> through ChatPromptTemplate see in this file

It is Used when we are Working with List of messages and in that list of messages we have to create Dynamic Messages. 
'''


from langchain_core.prompts import ChatPromptTemplate

# Caution : This Will Not Work in Langchain , while Creating Dynamic Message BuiltIn System ,Human Message placeholders Not Fill , not work.
# That' why Commented , see below code ,that work
'''
chat_template = ChatPromptTemplate([
    SystemMessage(content = 'You are a helpful {domain} expert'),
    HumanMessage(content = 'Explain in simple terms, what is {topic})
])
'''

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),  # Dynamic Message
    ('human', 'Explain in simple terms, what is {topic}') # Dynamic Messages
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)
