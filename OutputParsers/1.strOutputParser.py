# String Output prasers

## Genearting Summary {Without} Str Output Parse ##
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

# LLM define
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.18-Chat-v1.0",
    task='text-generation'
)

#Model Object Created
model = ChatHuggingFace(llm=llm)

# 1st Prompt 
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd Prompt
template2 = PromptTemplate(
    template="write a 5 line Summary on the follwing text. /n {text}",
    input_variables=['text']

)

prompt1 = template1.invoke({'topic':'black hole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})
result2 = model.invoke(prompt2)

# Printing Summary of Detailed Topic | result1 |prompt 1
print(result1.content)


#########################################################################################################
## Genearting Summary {With} Str Output Parse ##
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.18-Chat-v1.0",
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

# 1st Prompt
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt
template2 = PromptTemplate(
    template = "write a 5 line Summary on the follwing text. /n {text}",
    input_variables = ['text']
)

# Parser Form
parser = StrOutputParser()

# Chain Form
chain = template1 | model | parser | template2 | model | parser
 
result = chain.invoke({'topic': 'black hole'})

print(result)