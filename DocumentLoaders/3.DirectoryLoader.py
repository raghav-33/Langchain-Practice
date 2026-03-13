# What if we want read multiple pdf in folder at once
# it help to load multiple document from directory 
from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path = 'books',  # Directory Path
    glob = '*.pdf' ,  # tell the pattern to which files to read (*.pdf : indicate read all pdf files)
    loader_cls = PyPDFLoader # Tell the which type of loader , depend on files 
)

docs = loader.load()
print(len(docs))
print(docs[0].page_content)  # First Page | Document Content print
print(docs[0].metadata)

# Printing All document
for document in docs:
    print(document.metadata)

'''
PROBLEM : 
Major Problem we are facing here , loading of multiple files from directory 
takes lot of time . if no of files increases too much then time also increases too much
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        V
                    SOLUTION IS
                        |
                        |
                        |
                        |
                        |
                        |
                        V
                    Lazy Loading
 It return a generator , i.e : one element at a time and load next when needed and remove previous from memory.


'''


from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path = 'books',  # Directory Path
    glob = '*.pdf' ,  # tell the pattern to which files to read (*.pdf : indicate read all pdf files)
    loader_cls = PyPDFLoader # Tell the which type of loader , depend on files 
)

# Lazy Load
docs = loader.lazy_load()
print(len(docs))
print(docs[0].page_content)  # First Page | Document Content print
print(docs[0].metadata)

# Printing All document
for document in docs:
    print(document.metadata)

