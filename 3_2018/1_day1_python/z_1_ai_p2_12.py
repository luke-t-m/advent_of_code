"""You can solve this problem by creating a function that takes a list of numbers and returns the first number that appears twice in the list. Here is a possible implementation in Python:

"""
def first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None
"""

To use this function to solve the problem, you would first need to read the input from the file `1_input`. This can be done using the `open()` and `readlines()` functions in Python. For example:

"""
with open('1_input') as f:
    input_lines = f.readlines()
"""

This code reads the lines of the file `1_input` and saves them in the list `input_lines`. You can then parse this list of strings to extract the numbers that you need. To do this, you can use the `split()` method of the string class to split each string on the newline character (`'\n'`). This will give you a list of strings containing the individual numbers. You can then use the `map()` function to convert each string to an integer, and finally pass the resulting list to the `first_duplicate()` function to get the answer.

Here is the complete code:

"""
def first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None

with open('1_input') as f:
    input_lines = f.readlines()

# Split the input lines on the newline character and convert each string to an integer
numbers = list(map(int, input_lines[0].split('\n')))

# Get the first duplicate number
result = first_duplicate(numbers)

# Print the result
print(result)
"""

You can then run this code to get the answer to the problem."""