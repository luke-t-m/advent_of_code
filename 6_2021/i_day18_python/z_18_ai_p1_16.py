"""This problem can be solved by simulating the reduction process of snailfish numbers as described in the problem statement. To do this, we can create a function that takes a snailfish number as input and reduces it until it is in its reduced form. This function can be implemented as follows:

"""
def reduce(snailfish):
    # Keep reducing the snailfish number until no action applies
    while True:
        # Check if any pair is nested inside four pairs
        explode = False
        for i in range(len(snailfish)):
            if isinstance(snailfish[i], list) and len(snailfish[i]) == 2:
                if (i > 0 and isinstance(snailfish[i-1], list) and len(snailfish[i-1]) == 2 and
                    i > 1 and isinstance(snailfish[i-2], list) and len(snailfish[i-2]) == 2 and
                    i > 2 and isinstance(snailfish[i-3], list) and len(snailfish[i-3]) == 2):
                    # Explode the pair
                    snailfish[i] = 0
                    explode = True
                    if i > 0 and isinstance(snailfish[i-1], int):
                        snailfish[i-1] += snailfish[i-2][0]
                    if i < len(snailfish)-1 and isinstance(snailfish[i+1], int):
                        snailfish[i+1] += snailfish[i-2][1]
        if not explode:
            break

    # Check if any regular number is 10 or greater
    for i in range(len(snailfish)):
        if isinstance(snailfish[i], int) and snailfish[i] >= 10:
            # Split the regular number
            snailfish[i] = [snailfish[i] // 2, (snailfish[i] + 1) // 2]

# Read the snailfish numbers from the input file
with open('18_input') as f:
    snailfish1 = f.readline().strip()
    snailfish2 = f.readline().strip()

# Reduce the snailfish numbers
reduce(snailfish1)
reduce(snailfish2)

# Add the snailfish numbers and reduce the result
result = snailfish1 + snailfish2
reduce(result)

# Print the result
print(result)
"""

To parse the input snailfish numbers from the file, we can use a simple recursive function that takes a string representing a snailfish number as input and returns the corresponding list of numbers and pairs. This function can be implemented as follows:

"""
def parse_snailfish(s):
    # Initialize the result as an empty list
    result = []

    # Parse the snailfish number
    i = 0
    while i < len(s):
        # Check if the current character is a digit
        if s[i].isdigit():
            # Parse the regular number
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            result.append(num)
        elif s[i] == '[':
            # Parse the pair
            i