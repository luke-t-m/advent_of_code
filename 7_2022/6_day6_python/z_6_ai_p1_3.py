"""The following code reads the input from the file `6_input` and prints the number of characters from the beginning of the buffer to the end of the first such four-character marker.

"""
# Read the input from the file `6_input`.
with open("6_input", "r") as f:
    data = f.read()

# Initialize a list `last_four` to track the last four characters received.
last_four = []

# Iterate over the characters in the input data.
for i, ch in enumerate(data):
    # Add the current character to `last_four`.
    last_four.append(ch)

    # If `last_four` contains more than four characters, remove the first character.
    if len(last_four) > 4:
        last_four.pop(0)

    # If the last four characters in `last_four` are all different, print the
    # current index and exit the loop.
    if len(set(last_four)) == 4:
        print(i)
        break
""""""