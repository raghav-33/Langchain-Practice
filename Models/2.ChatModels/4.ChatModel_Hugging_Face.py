# HUGGING FACE

#---------------- Hugging Face API Method ---------------- #

# Neccesary Imports
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()


# LLM define
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# Object Created
model = ChatHuggingFace(llm = llm)

# Model calling
result = model.invoke("What is the Capital of India ?")

# Print Result
print(result.content)


#---------------- Hugging Face Local Download Method ---------------- #
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)