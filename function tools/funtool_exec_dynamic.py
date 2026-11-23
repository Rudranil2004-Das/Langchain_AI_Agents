from langchain_openai import ChatOpenAI
from mytool import add_numbers,multiply_numbers


llm=ChatOpenAI(
    model='gpt-6-astra',
    )

llm_with_tool=llm.bind_tools([add_numbers])


response=llm_with_tool.invoke('what is 125 plus 345 ? Use the tool add_numbers')


print("Text: ",response.content)
print("Tool Requests: ",response.tool_calls)


# for call in response.tool_calls:
#     if call['name']=='add_numbers':
#         result=add_numbers.invoke(call['args'])
#         print('Python Result: ',result)

for call in response.tool_calls:
    print(f"LLM requested: {call['name']} with args {call['args']}")
    choice = input('choice? (add_no / multi_no): ').strip()

    match choice:
        case 'add_numbers':
            print('Python add Result: ', add_numbers.invoke(call['args']))
        case 'multiply_numbers':
            print('Python multiply Result: ', multiply_numbers.invoke(call['args']))
        case _:
            print("NA")