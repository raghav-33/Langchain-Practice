# Json Output Parser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.18-Chat-v1.0",
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me name , age and city of a fictional person \n {format_instruction}',  # We have to pass additional paramter which tell, in which format we want output
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}     #A partial variable in LangChain is a prompt variable whose value is pre-filled at template creation time, so the user or chain does not need to provide it at runtime. 
)

chain = template | model | parser 
result = chain.invoke({})  # Pass Empty dict since no external input varible from user

print(result)

''' 
NOTE :
with the help of json output parser we can get json object 
but problem is we {cannot enforce any Schema} when pass any external input variable from user 

SOLUTION OF PROBLEM : structured output parsers

'''

