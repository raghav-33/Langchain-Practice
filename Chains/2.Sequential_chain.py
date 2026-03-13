# Sequential Chain 
# Calling 2 times LLM (sending output of LLM to LLM for further Processing)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import StrOutputParser

load_dotenv()

# Step 1 : Prompt
# prompt 1
prompt1 = PromptTemplate(
    template = 'Generate a deatailed report on {topic}',
    input_variables = ['topic']
)

# Prompt 2
prompt2 = PromptTemplate(
    template = "Generate a 4 point summary from the following text \n {text}",
    input_variables=['text']
)

# Step 2 : Model
model = ChatOpenAI()

# Step 3 : Parser
parser = StrOutputParser()

# Step 4 : chain
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'unemployment in India'})

print(result)
