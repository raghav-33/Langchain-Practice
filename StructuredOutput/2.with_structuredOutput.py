from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

# Model Created
model = ChatOpenAI()


# Schema Created For Structured Output
class Review(TypedDict):
    summary : str
    sentiment : str
structured_model = model.with_structured_output(Review)


# Model Invoke
result = structured_model.invoke("This smartphone delivers a smooth performance with a responsive display and long-lasting battery life.The camera captures sharp, vibrant photos, making it a great choice for everyday use")

print(result)
print(type(result))
print(result['summary'])
print(result['sentiment'])

###############################Annotated#######################################################################
'''Since our LLM is trained it will genearted Structured output as above, behind the scences system prompt is given to LLM and our prompt attach with that.
   But let us assume Due to some Issues it will not generated structured output . eg: it is not geneartaing summary in place of Summary
   so We can {Explicitly Mention Prompt} in our Code 
   With the help of {Annotated}

NOTE : Full code is same as above only Annotated Definition Extra Given
       Annotated Definition = Explict Prompt   
'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated

load_dotenv()

# Model Created
model = ChatOpenAI()


# Schema Created For Structured Output
class Review(TypedDict):
    summary : Annotated[str,"A Brief Summary of the review"]
    sentiment : Annotated[str,"Return Sentiment of Review Either Positive , Negative or Netural"]
structured_model = model.with_structured_output(Review)


# Model Invoke
result = structured_model.invoke("This smartphone delivers a smooth performance with a responsive display and long-lasting battery life.The camera captures sharp, vibrant photos, making it a great choice for everyday use")

print(result)
print(type(result))
print(result['summary'])
print(result['sentiment'])


#############################Complex Structured output#######################################################################
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional

load_dotenv()

# Model Created
model = ChatOpenAI()


# Schema Created For Structured Output
class Review(TypedDict):
    summary : Annotated[str,"A Brief Summaryof the review"]
    sentiment : Annotated[str,"Return Sentiment of Review Either Positive , Negative or Netural"]
    pros : Annotated[Optional[list[str]],"Write Down all the Pro's Inside a list"]  ## Pros are Optional , Some mobiles have or some not
    cons : Annotated[Optional[list[str]],"Write Down all the Con's Inside a list"]

structured_model = model.with_structured_output(Review)


# Model Invoke
result = structured_model.invoke("This smartphone delivers a smooth performance with a responsive display and long-lasting battery life.The camera captures sharp, vibrant photos, making it a great choice for everyday use")

print(result)
print(type(result))
print(result['summary'])
print(result['sentiment'])
   
'''NOTE: In this Method There is No gurantted of Structured Output and 
         We Have to Put {Data validation} , we cannot put here.
         For {Data validation} We Use : pydantic
'''