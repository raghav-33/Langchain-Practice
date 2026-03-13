from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()
model = ChatOpenAI()

#Schema
class Review(BaseModel):
    key_themes : list[str]  = Field(description="Write down all the key themes discussed in the review in a list ")
    summary: str  = Field(description = "A brief Summary of the Review")
    sentiment: str  = Field(description ="A Sentiment can either positive,negative or neutral")
    pros: Optional[list[str]]  = Field(deafult = None , description ="write down all the pros inside a list")
    cons: Optional[list[str]]  = Field(deafult = None , description ="write down all the Cons inside a list" )

structured_model = model.with_structured_output(Review)


# Model Invoke
result = structured_model.invoke("This smartphone delivers a smooth performance with a responsive display and long-lasting battery life.The camera captures sharp, vibrant photos, making it a great choice for everyday use")

print(result)

