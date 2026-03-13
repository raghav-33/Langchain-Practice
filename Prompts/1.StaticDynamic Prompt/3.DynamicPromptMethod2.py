# Dynamic Prompt Template : Method 2
'''
Why Method 2 ?
In Previous Method We create our Dynamic Prompt in same File as Main code
Due to which file Become messy 

NOTE : 
We can Create Our Dynamic Prompt in Sepearte File and Call it in main file
'''

'''
Setup 
DynamicPromptMethod2: Main Code File
PromptGenerator : Template Generator File
NOTE: In this file we call our Prompt Template File
'''



from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st  # type: ignore
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI()

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# Calling / Loading Dynamic Prompt File
template=load_prompt('template.json') 


# Fill the Placeholders
prompt = template.invoke({
   'paper_input':paper_input,
   'style_input':style_input,
   'length_input':length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result)