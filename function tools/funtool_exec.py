from langchain_openai import ChatOpenAI
from mytool import add_numbers,multiply_numbers


llm=ChatOpenAI(
    model='gpt-6-astra',
    )

llm_with_tool=llm.bind_tools([add_numbers])


response=llm_with_tool.invoke('what is 125 plus 345 ? Use the tool add_numbers')


print("Text: ",response.content)
print("Tool Requests: ",response.tool_calls)


for call in response.tool_calls:
    if call['name']=='add_numbers':
        result=add_numbers.invoke(call['args'])
        print('Python Result: ',result)