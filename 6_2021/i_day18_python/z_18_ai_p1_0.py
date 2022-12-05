"""The following code is a possible solution to the problem. It reads the input from the file `18_input`, performs the required operations, and prints the result.

"""
from collections import deque

# Function to explode a pair
def explode(p):
    # Get the left and right values of the pair
    left, right = p[0], p[1]
    
    # Initialize the result as the pair [0, 0]
    res = [0, 0]
    
    # If there is a regular number to the left of the pair,
    # add the left value of the pair to it
    if left and not isinstance(left[0], list):
        left[0] += p[0][0]
    
    # If there is a regular number to the right of the pair,
    # add the right value of the pair to it
    if right and not isinstance(right[0], list):
        right[0] += p[1][0]
    
    return res

# Function to split a regular number
def split(n):
    # Divide the number by two, rounding down for the left element
    # and rounding up for the right element
    return [n // 2, (n + 1) // 2]

# Function to reduce a snailfish number
def reduce(num):
    # If the number is a pair, check if it needs to be exploded
    if isinstance(num, list):
        # Count the number of pairs that the pair is nested inside
        count = 0
        x = num
        while isinstance(x, list):
            x = x[0]
            count += 1
        
        # If the pair is nested inside four pairs, explode it
        if count == 4:
            return explode(num)
        
        # Otherwise, reduce the left and right values of the pair
        # and return the reduced pair
        return [reduce(num[0]), reduce(num[1])]
    
    # If the number is a regular number, check if it needs to be split
    elif num >= 10:
        # If the number is 10 or greater, split it
        return split(num)
    
    # Otherwise, the number is already reduced, so return it as is
    return num

# Read the input from the file 18_input
with open('18_input') as f:
    # Parse the input and store the two snailfish numbers
    num1 = eval(f.readline())
    num2 = eval(f.readline())

# Perform the addition
result = [num1, num2]

# Reduce the result until no more actions can be performed
while True:
    # Reduce the result
    result = reduce(result)
    
    # Check if any actions were performed during the reduction
    if result == reduce(result):
        break

# Print the reduced result
print(result)
""""""