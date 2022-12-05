"""The following python code solves the problem described above.

"""
# Read the input from the file 18_input
with open("18_input", "r") as file:
    snailfish_number = file.readline()

# Helper function to split a number if it is greater than or equal to 10
def split(n):
    if n >= 10:
        return [n//2, n//2 + n % 2]
    return n

# Helper function to explode a pair
def explode(pair):
    left_val, right_val = pair
    left_num, right_num = None, None
    if isinstance(left_val, list):
        left_num = explode(left_val)
    if isinstance(right_val, list):
        right_num = explode(right_val)
    if left_num is not None:
        left_val = left_num
    if right_num is not None:
        right_val = right_num
    if left_val >= 10:
        left_val = split(left_val)
    if right_val >= 10:
        right_val = split(right_val)
    if isinstance(left_val, list) and isinstance(right_val, list):
        return [left_val, right_val]
    return [left_val, right_val]

# Helper function to reduce a snailfish number
def reduce_number(snailfish_number):
    # If the snailfish number is a single number, split it if it is >= 10
    if not isinstance(snailfish_number, list):
        return split(snailfish_number)
    # If the snailfish number is a pair, explode it
    left_val, right_val = snailfish_number
    left_num, right_num = None, None
    if isinstance(left_val, list):
        left_num = reduce_number(left_val)
    if isinstance(right_val, list):
        right_num = reduce_number(right_val)
    if left_num is not None:
        left_val = left_num
    if right_num is not None:
        right_val = right_num
    if left_val >= 10:
        left_val = split(left_val)
    if right_val >= 10:
        right_val = split(right_val)
    if isinstance(left_val, list) and isinstance(right_val, list):
        return explode(left_val + right_val)
    return [left_val, right_val]

# Add the two snailfish numbers and reduce the result
result = reduce_number(snailfish_number + snailfish_number)

# Print the result
print(result)
""""""