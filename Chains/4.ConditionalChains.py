# Conditional Chains

''''
What We Built ?
Person give a feedback about a product . 
our system will analyze feedback whether it is positive or negative . 
if feedback is positive sytem will reply thanks , 
if negative then reply we will connect will customer care.
'''

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
# For Making Conditional Branches 
from langchain_core.runnables import RunnableBranch , RunnableLamda

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

# For Getting Structured Output (either Positive | Negative)
class Feedback(BaseModel):
    sentiment: Literal['positive' , 'negative'] = Field(description = "Give the Sentiment of Feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate (
    template = 'Classify the sentiment of follwing feedback text either positive or negative \n {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction' : parser2.get_format_instructions()}
)
classifier_chain = prompt1 | model | parser2



prompt2  = PromptTemplate(
    template = "Write an Appropirate Response to positive feedback \n {feedback}",
    input_variables = ['feedback']
)
prompt3  = PromptTemplate(
    template = "Write an Appropirate Response to Negative feedback \n {feedback}",
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment  == 'positive' , prompt2 | model | parser),  # indicate If condt 1 is True then Execute this Chain
    (lambda x:x.sentiment  == 'negative' , prompt3 | model | parser),  # indicate If condt 2 is True then Execute this Chain
     lambda x: "Could not find sentiment"        # Deafult Chain , If any Condition is not true then execute it.
)


chain = classifier_chain | branch_chain
result = chain.invoke({'feedback' : 'This is a Terrible phone'})
print(result)

chain.get_graph().print_ascii()