
from langchain_openai import OpenAIEmbeddings

llm=OpenAIEmbeddings()

text = input("Enter the text")
response = llm.embed_query(text)
print(response)