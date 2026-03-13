# Runnable PassThrough 

'''
What we are going to do ?
we give to LLM a topic to generate a joke about topic.
LLM give generate a Joke
then We pass Same Joke To LLM to explain it 
we want result show in form of first Joke9done through Runnable pass Through) which show as its generated joke
then its explaination (by sequential and parallel runnable)
'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Runnable Sequence , parallel and passThrough import
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(), # Joke pass as its to for explantion processing
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))
