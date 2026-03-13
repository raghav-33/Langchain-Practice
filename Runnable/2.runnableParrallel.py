# Runnable Parallel Implemantation

'''
What we are Going to Built ?
we have 1 LLMs . we give to LLM a topic . LLM will generate tweet about topic
and LLM  will  also generate Linkedin post about topic {parallely / simultaneously}
and display us result as dictionary of tweet and linkedin post
'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Runnable Sequence and parallel import
from langchain_core.runnables import RunnableSequence , RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a tweet about {topic}",
    input_variables = ['topic']
) 

prompt2 = PromptTemplate(
    template = "Generate a Linkedin post about {topic}",
    input_variables = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
        'tweet' : RunnableSequence(prompt1 , model , parser),
        'linkedin' : RunnableSequence(prompt2 , model , parser)
    })

result = parallel_chain.invoke({'topic':'AI'})
print(result)
print(result['tweet']) # Show only tweet post
print(result['linkedin']) # show Only Linkedin Post






