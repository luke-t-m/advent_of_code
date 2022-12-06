"""To solve this problem, we can iterate over the characters in the input string, keeping track of the last four characters that have been processed. If at any point the last four characters are all different, we can return the number of characters that have been processed so far, which is the solution to the problem.

Here is one way to solve the problem in Python:

"""
# Read the input string from the file
with open("6_input", "r") as f:
    s = f.read().strip()

# Iterate over the characters in the input string
for i, c in enumerate(s):
    # If the last four characters are all different, return the solution
    if len(set(s[i-3:i+1])) == 4:
        print(i+1)
        break
""""""