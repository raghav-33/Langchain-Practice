''' 
What we are going to build 
We are given Detailed long text about topic 
we will generate notes from that and also quiz and show to user 
'''

# Parallel Chains 
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import StrOutputParser
# For Making parllel chain and execute it simultaneously we need {Runnable Parallel}
from langchain_core.runnables import RunnableParallel 

load_dotenv()

# Step 1 : Prompt
prompt1 = PromptTemplate(
    template = "Generate a short and simple notes from follwing text \n {text}",
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = "Generate a 7 short Question Answer From follwing Text \n {text}",
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template ="Merge the Provided notes and quiz into Single Document \n notes -> {notes} and quiz -> {quiz}",
    input_variables = ['notes','quiz']
)

# Step2 : Model
model1 = ChatOpenAI()
model2 = ChatAnthropic(model ='claude-3')

# Step3 : Parser
parser = StrOutputParser()

# Step4 : Chain
parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser ,   # notes : name given to chain 1
    'quiz' : prompt2 | model2 | parser 
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain



text = """ Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.
The advantages of support vector machines are:
Effective in high dimensional spaces.
Still effective in cases where number of dimensions is greater than the number of samples.
Uses a subset of training po ints in the decision function (called support vectors), so it is also memory efficient.
Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.
The disadvantages of support vector machines include:
If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.
SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).
The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered """

result = chain.invoke({'text':text})
print(result)