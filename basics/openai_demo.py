
from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-6-astra", )
question = input("Enter the question")
response = llm.invoke(question)
print(response.content)