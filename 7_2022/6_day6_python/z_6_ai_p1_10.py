"""The problem can be solved as follows:

1. Read the input string from the file `6_input`.
2. Iterate over the characters in the input string.
3. For each character, append it to a list of the four most recently received characters.
4. If the list of the four most recently received characters contains four different characters, return the length of the input string minus four.

Here is the solution in Python:

"""
# Read the input string from the file
with open('6_input') as f:
    input_str = f.read().strip()

# Iterate over the characters in the input string
four_most_recent = []
for c in input_str:
    # Append the character to the list of the four most recently received characters
    four_most_recent.append(c)
    # If the list contains four different characters, return the length of the input string minus four
    if len(set(four_most_recent)) == 4:
        print(len(input_str) - 4)
        break
""""""