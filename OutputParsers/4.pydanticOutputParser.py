from langchain_huggingface.chat_models import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.18-Chat-v1.0",
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name : str  = Field(description="name of the Person")
    age : int  = Field(gt = 18 ,description="Age of the Person")
    city : str  = Field(description="City of the Person")

parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = "Generate the name , age and city of fictional {place} person \n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions':parser.get_format_instructions}

)

# This time Writing Without chain
prompt = template.invoke(template)
result=model.invoke(prompt)
finalResult=parser.parse(result.content) 

print(finalResult)