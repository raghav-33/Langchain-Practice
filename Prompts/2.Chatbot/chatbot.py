# Chatbot Application | APP

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()

model = ChatOpenAI()

while True:
    user_input = input("You: ")
    if user_input == 'exit' :
        break
    result = model.invoke(user_input)
    print("A.I: ",result.content)

''' Problem : In above Code(chatbot) is it not remember chat history '''



#-------------ChatBot with Chat History-----------------------------------------------#

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()

model = ChatOpenAI()
chat_history = []  # Maintaing a Dictinary to Store ChatHistory
 
while True:
    user_input = input("You: ")
    chat_history.append(user_input)

    if user_input == 'exit' :
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)  # appending result in chathistory
    print("A.I: ",result.content)

print(chat_history)

''' Now Problem is In chat history we cannot identified which message is send by user or chatbot itself
    as Chat history become large it would become difficult for chatbot to remeber which message is send by him or user
    and further it hullicinate
'''

''' How to resolve this Issue ?
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               |
               🠇
        Use {Message} Component

Note: LangChain Provide Message Component For it.
       (i) First see Message Component File then shift here
       (ii) Now Construct chatbot with Message Class
'''
#-------------ChatBot with Chat History + Messages-----------------------------------------------#

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

model = ChatOpenAI()
chat_history= [
    SystemMessage(content = "You are Helpful A.I assitant") 
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input))  # convert user input to user message

    if user_input == 'exit' :
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))  # appending result in chathistory and converting it Ai message
    print("A.I: ",result.content)

print(chat_history)

