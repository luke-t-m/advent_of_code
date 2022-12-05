"""The following code can be used to solve the problem described above in Python.

"""
def reduce_number(number):
    # If number is a pair
    if isinstance(number, list):
        # If the pair is nested inside four pairs
        if all(isinstance(x, list) for x in number[:4]):
            # Explode the pair
            left_number = number[4][0]
            right_number = number[4][1]
            # Add the pair's left value to the first regular number to the left of the exploding pair (if any)
            if isinstance(left_number, int):
                number[3][1] += left_number
            # Add the pair's right value to the first regular number to the right of the exploding pair (if any)
            if isinstance(right_number, int):
                number[5][0] += right_number
            # Replace the exploding pair with the regular number 0
            number[4] = 0
        else:
            # Recursively reduce the elements of the pair
            number[0] = reduce_number(number[0])
            number[1] = reduce_number(number[1])
    # If number is a regular number
    elif isinstance(number, int):
        # If the regular number is 10 or greater
        if number >= 10:
            # Split the regular number
            left_number = number // 2
            right_number = (number + 1) // 2
            number = [left_number, right_number]
    return number

def reduce(number):
    # Reduce the number until no further reduction is possible
    while True:
        reduced_number = reduce_number(number)
        if reduced_number == number:
            break
        number = reduced_number
    return number

# Read input from file
with open('18_input') as f:
    input_lines = f.readlines()

# Parse input
numbers = []
for line in input_lines:
    # Parse each line as a snailfish number
    number = eval(line.strip())
    # Reduce the number
    reduced_number = reduce(number)
    # Add the reduced number to the list of numbers
    numbers.append(reduced_number)

# Print the reduced numbers
print(numbers)
""""""