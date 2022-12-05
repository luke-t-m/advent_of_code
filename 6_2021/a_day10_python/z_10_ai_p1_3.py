"""The following code will solve the problem.

"""
# Read the input file
with open("10_input") as f:
    lines = f.readlines()

# Define the legal closing characters for each opening character
closers = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

# Keep track of the total score
total_score = 0

# Iterate over each line in the input
for line in lines:
    # Keep track of the score for this line
    score = 0
    
    # Keep track of the currently open chunks
    open_chunks = []

    # Iterate over each character in the line
    for char in line:
        # If the character is an opening character, add it to the list of open chunks
        if char in closers:
            open_chunks.append(char)
            score += 1
        # If the character is a closing character, check if it matches the last opening character
        elif char in closers.values():
            # If it doesn't match, stop processing this line
            if open_chunks and closers[open_chunks[-1]] != char:
                break
            # If it does match, remove the last opening character from the list of open chunks
            else:
                open_chunks.pop()
    # If there are no open chunks at the end of the line, add the score for this line to the total score
    if not open_chunks:
        total_score += score

# Print the total score
print(total_score)
""""""