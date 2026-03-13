# Runnable Sequence Implemantation

######################### Single Sequence Chain Implemantion #################################
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Runnable Sequence import
from langchain_core.runnables import RunnableSequence

load_dotenv()


prompt = PromptTemplate(
    template = "Write a Joke about {topic}",
    input_variables=['topic']
)

model = ChatOpenAI()
parser = StrOutputParser()

#Runnable Sequence
chain = RunnableSequence(prompt , model , parser)
result = chain.invoke({'topic' : 'AI'})
print(result)





######################### Multiple Sequence Chain Implemantion #################################
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Runnable Sequence import
from langchain_core.runnables import RunnableSequence

load_dotenv()


prompt1 = PromptTemplate(
    template = "Write a Joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following  joke : {text}",
    input_variables=['text']
)

model = ChatOpenAI()
parser = StrOutputParser()

# Runnable Sequence :  { Multiple Chain Implemanation }
chain = RunnableSequence(prompt1 , model , parser , prompt2 ,model , parser)
result = chain.invoke({'topic' : 'AI'})
print(result)
