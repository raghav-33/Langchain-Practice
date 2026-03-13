# Biggest benfit of Structured Output Parser is we can Enforce a Schema
from langchain_huggingface.chat_models import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.18-Chat-v1.0",
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name = 'fact1' , description = "Fact 1 about the topic"),
    ResponseSchema(name = 'fact2' , description = "Fact 2 about the topic"),
    ResponseSchema(name = 'fact3' , description = "Fact 3 about the topic")
]
parser = StructuredOutputParser.from_response_schemas(schema)


template =  PromptTemplate(
    template = 'Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= {'format_instruction':parser.get_format_instructions()}
)

chain = template | model |parser
result = chain.invoke({'topic':'black hole'})
print(result)

'''
NOTE : 
Main Problem of This : we can't do {Data Validation} 

SOLUTION : pydantic Output Parser
'''