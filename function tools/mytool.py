from langchain_core.tools import tool

@tool # @tool is the DECORATOR placed on top of function
def add_numbers(first: float, second: float) -> float:
    'Add 2 numbers and return the total------> TYPE HINT'
    return first+second


@tool # @tool is the DECORATOR placed on top of function
def multiply_numbers(first: float, second: float) -> float:
    'multiply 2 numbers and return the product---> TYPE HINT'
    return first*second

print(add_numbers.name)
print(add_numbers.description)
print(add_numbers.args)

print('-------------------\n\n\n')