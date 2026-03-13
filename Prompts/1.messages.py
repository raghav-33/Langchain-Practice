'''
MESSAGES:
In LangChain, a Message represents one piece of conversation sent to or from an LLM.

Think of it as:
🗣️ Who said what in a conversation

LangChain doesn't just send plain text to chat models (like ChatGPT).
Instead, it sends structured messages so the model understands:

Who is speaking
What role they have
What the intention is

'''

''' TYPES OF MESSAGES IN LANGCHAIN
Langchain Provide 3 types of Messages (i). SystemMessage (ii)HumanMesssage (iii)A.I Messsage
(i). Human Message : Message Send by user or What the user says.
(ii). A.I Message : User Query Responds By A.I
(iii). System Message : Sets behavior / rules for the model . eg : act as Proffesional Doctor

'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

load_dotenv()

model = ChatOpenAI()

messages  = [
    SystemMessage(content="You are a Helpful assistant"),
    HumanMessage(content="Tell me About a langchain")
]

result = model.invoke(messages)
Ai=AIMessage(content = result.content)
messages.append(Ai)

print(messages)