from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
# Model / Object created
model=ChatOpenAI()

# Header Show in Ui like Html Header tags
st.header("Research Tool")

# Text box Show: higlighting Enter your Prompt
user_input = st.text_input("Enter Your Prompt")

# Summarize button : when user click on it button , Prompt Send to model
if st.button("Summarize"):
    # Model Calling
    result = model.invoke(user_input)
    st.write(result.content)
