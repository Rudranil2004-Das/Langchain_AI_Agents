from langchain_ollama import ChatOllama

llm=ChatOllama(model="tinyllama")

question = input("Enter the question")
response = llm.invoke(question)
print(response.content)

