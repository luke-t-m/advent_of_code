"""Here's a solution in Python:

"""
# Open the input file and read the lines
with open("10_input", "r") as f:
    lines = f.readlines()

# Initialize the scores
scores = []

# Loop over each line
for line in lines:
    # Initialize a list to keep track of the characters we find
    chars = []
    
    # Initialize a variable to keep track of the score for this line
    score = 0
    
    # Initialize a variable to keep track of whether this line is corrupted
    corrupted = False
    
    # Loop over each character in the line
    for c in line:
        # If the character is one of the opening characters, add it to the list
        if c in "([{<":
            chars.append(c)
        # Otherwise, if the character is one of the closing characters
        elif c in ")]}>":
            # If the list is empty, the line is corrupted
            if len(chars) == 0:
                corrupted = True
                break
            # If the last character in the list doesn't match the current character, the line is corrupted
            if chars[-1] != c:
                corrupted = True
                break
            # If the last character in the list does match the current character, remove it from the list
            # and add the appropriate score
            else:
                chars.pop()
                if c == ")":
                    score += 3
                elif c == "]":
                    score += 57
                elif c == "}":
                    score += 1197
                elif c == ">":
                    score += 25137
    
    # If the list is not empty, the line is corrupted
    if len(chars) > 0:
        corrupted = True
    
    # If the line is not corrupted, add its score to the list of scores
    if not corrupted:
        scores.append(score)

# Print the sum of the scores
print(sum(scores))
""""""