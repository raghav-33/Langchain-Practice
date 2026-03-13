# Length Based Text Splitter
from langchain.text_splitter import CharacterTextSplitter

text = """ For those who are interested in finding random paragraphs, thats exactly what this webpage provides. 
If both a random word and a random sentence aren't quite long enough for your needs, then a random paragraph might be the perfect solution. 
Once you arrive at this page, 
you'll see a random paragraph. 
If you need another one, all you need to do is click on the "next paragraph" button. 
If you happen to need several random paragraphs all at once, you can use this other paragraph generator. 
Below you can find a number of ways that this generator can be used."""


splitter = CharacterTextSplitter(
    chunk_size = 100, # splitting on every 100th character
    chunk_overlap = 0,
    seperator = ''     
)

result = splitter.split_text()
print(result)


############################### Actuall PDF Working #######################################
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
docs=loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100, # splitting on every 100th character
    chunk_overlap = 0,
    seperator = ''     
)

result = splitter.split_documents(docs)
print(result)    # All chunks
print(result[0]) # First Chunk
