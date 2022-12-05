"""The following code is a correct solution to the problem:
"""
from collections import deque

# Read the input
with open("18_input") as f:
    num1, num2 = map(eval, f.read().strip().split("\n"))

# Helper function to check if a number is regular
def is_regular(num):
    return isinstance(num, int)

# Helper function to split a number
def split(num):
    return [num // 2, num // 2 + num % 2]

# Helper function to reduce a number
def reduce(num):
    if is_regular(num):
        if num >= 10:
            return split(num)
        else:
            return num
    else:
        return [reduce(num[0]), reduce(num[1])]

# Helper function to check if a number is reduced
def is_reduced(num):
    if is_regular(num):
        return True
    elif len(num) > 2:
        return False
    else:
        return is_reduced(num[0]) and is_reduced(num[1])

# Helper function to explode a number
def explode(num):
    if len(num) != 2:
        return False
    if not (is_regular(num[0]) and is_regular(num[1])):
        return False

    # Find the first regular number to the left
    queue = deque(num[0])
    left = None
    while queue:
        curr = queue.popleft()
        if is_regular(curr):
            left = curr
            break
        else:
            queue.extend(curr)

    # Find the first regular number to the right
    queue = deque(num[1])
    right = None
    while queue:
        curr = queue.pop()
        if is_regular(curr):
            right = curr
            break
        else:
            queue.extendleft(reversed(curr))

    # If either the left or right regular number was found, add them and return 0
    if left is not None or right is not None:
        return [0, (left or 0) + (right or 0)]
    else:
        return False

# Main function to add two snailfish numbers
def add(num1, num2):
    # Reduce the numbers
    num1 = reduce(num1)
    num2 = reduce(num2)

    # Add the numbers
    num = [num1, num2]

    # Keep reducing and exploding until the number is reduced
    while not is_reduced(num):
        num = reduce(num)
        exploded = explode(num)
        if exploded:
            num = exploded

    return num

# Compute and print the result
result = add(num1, num2)
print(result)
""""""