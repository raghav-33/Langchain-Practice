from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import StrOutputParser

load_dotenv()


#  1. Prompt Template Define
prompt = PromptTemplate(
    template = 'Genearate 7 intersting facts about {topic}',
    input_variables = ['topic']
)

# 2. Model Define
model = ChatOpenAI()

# 3. Parser
parser = StrOutputParser()

# 4. Chain create
chain = prompt | model |parser


# Chain Invoke
result = chain.invoke({'topic':'cricket'})

# Visulazing Chain
chain.get_graph().print_ascii()

# result print
print(result)