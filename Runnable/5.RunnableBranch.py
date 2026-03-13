'''
WHAT WE ARE GOING TO BUILT ?
we give a topic to llm to generate a report 
if report word length greater than 400
 we agin give to LLM summarize it .
'''

''' RunnablrBranch is like : conditional Statements 
    what to do when condition is True. 
'''


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

report_gen_chain = RunnableSequence(prompt1 , model , parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500 , RunnableSequence(prompt2 , model , parser)),  # 1.If Condition
    RunnablePassthrough()     # 2. Else Condition  if LEN < 500 print as it is.

    )

final_chain = RunnableSequence(report_gen_chain , branch_chain)
result =final_chain.invoke({'topic'  'AI'})
print(result)