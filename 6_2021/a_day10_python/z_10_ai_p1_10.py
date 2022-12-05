"""To solve this problem, we need to read the input from a file called `10_input`, then iterate through each line of the input and check if it is corrupted. A line is considered corrupted if it contains a chunk that opens with one of the four legal pairs of matching characters, but closes with a different one. If a line is corrupted, we need to stop at the first incorrect closing character on that line and return the syntax error score for that character.

Here is a solution in Python:

"""
# Read input from file
with open("10_input") as f:
    lines = f.readlines()

# Define a dictionary mapping opening characters to their corresponding closing characters
closing_chars = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

# Define a dictionary mapping illegal closing characters to their syntax error scores
error_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

# Iterate through each line of the input
for line in lines:
    # Keep track of the syntax error score for this line
    score = 0
    
    # Keep track of the current chunk of text that we are processing
    chunk = ""

    # Iterate through each character in the line
    for c in line:
        # If the character is an opening character, start a new chunk
        if c in closing_chars:
            chunk = c
        # If the character is a closing character and it doesn't match the corresponding
        # opening character for the current chunk, the line is corrupted
        elif c in closing_chars.values() and c != closing_chars[chunk[0]]:
            # Set the syntax error score for this line to the score for the incorrect
            # closing character
            score = error_scores[c]
            # Stop processing this line
            break
        # If the character is a closing character and it matches the corresponding
        # opening character for the current chunk, close the current chunk
        elif c in closing_chars.values() and c == closing_chars[chunk[0]]:
            chunk = ""

    # If the syntax error score for this line is non-zero, print it
    if score > 0:
        print(score)
""""""