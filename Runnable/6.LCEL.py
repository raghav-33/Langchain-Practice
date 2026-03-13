# Langchain Expression Language
'''
What is it ?
Langchain team Runnable Sequence is mostly commonly used runnable
so to make it easy Langchain team replace 
Runnable Sequence Syntax With "pipe operator ( | )"
'''

# Same app as Runnable Branch But only { syntax } changed

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Runnable Sequence , parallel and passThrough import
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough, RunnableLambda , RunnableBranch

load_dotenv()



prompt1 = PromptTemplate(
    template='Write a detailed report about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarizing the Follwoing text \n {text}',
    input_variables=['text']
)


model = ChatOpenAI()

parser = StrOutputParser()

report_gen_chain = prompt1|model|parser  # LCEL Syntax

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500 , prompt2|model|parser),  # 1.If Condition
    RunnablePassthrough()     # 2. Else Condition  if LEN < 500 print as it is.

    )

final_chain = RunnableSequence(report_gen_chain , branch_chain)
result =final_chain.invoke({'topic'  'AI'})
print(result)