# Runnable Lambda
''' 
Help to connvert Python Function into Runnable ,
which help in making chain by connecting with other runnables. 
'''

''''
  WHAT WE ARE GOING TO BUILT ?
  we will give topic to LLM to generate a topic  . we will create parrallel chain 
  in which first block we print joke as it is through help of runnable passthrough
  in 2nd block we creqate  runnable lambda which receive the joke and count no of word in joke.
  and then we combine both runnables and print the result which show first joke then no of words in it.
'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Runnable Sequence , parallel and passThrough import
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough, RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = ({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count) # or RunnableLambda(lambda x: (len(x.split()) ))
})

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)
result = final_chain.invoke({'topic':'Ai'})
print(result)