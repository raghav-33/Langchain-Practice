# Web Base Loader
# Used to Query over Webpages | Load Web Page Data | extract text content from webPages
# It uses 2 internal Libraries :
# (i) Beautiful Soup : Help to understand Html Structure of webpage.
#  (ii) Request library
# Disadvanteges :  Work Well only With Static Web Pages . Not good with web page which is javascript heavy (lots of action based on user click with javascript)
# Solution : To solve this use {SeleniumURLLoader}

from langchain_community.document_loaders import WebBaseLoader

url = "https://www.youtube.com/watch?v=bL92ALSZ2Cg&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=12"
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content )