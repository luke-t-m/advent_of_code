"""The solution to this problem is to read the input from the file "1_input", parse it to extract the frequency changes, then repeatedly sum the changes until the resulting frequency is reached twice. Here is a simple solution in Python that does this:

"""
# Read the input from the file "1_input"
with open("1_input") as f:
    lines = f.readlines()

# Parse the input to extract the frequency changes
changes = [int(x) for x in lines]

# Repeatedly sum the changes until the resulting frequency is reached twice
seen = set()
current = 0
while True:
    for change in changes:
        current += change
        if current in seen:
            print(current)
            exit()
        seen.add(current)
"""

This solution will print the first frequency reached twice and then exit."""