# open input file
f = open('10_input', 'r')

# initialize variable to store the score
score = 0

# go through each line in the file
for line in f:
    # initialize variable to store the stack of characters
    stack = []

    # go through each character in the line
    for char in line:
        # if the character is an opening character, push it to the stack
        if char in ['(', '[', '{', '&lt;']:
            stack.append(char)
        # otherwise, if the character is a closing character
        elif char in [')', ']', '}', '&gt;']:
            # if the stack is empty, the line is corrupted, so we can break out of the loop
            if not stack:
                break
            # pop the last character from the stack
            last_char = stack.pop()
            # if the last character is not the matching opening character, the line is corrupted
            if (last_char == '(' and char != ')') or (last_char == '[' and char != ']') or (last_char == '{' and char != '}') or (last_char == '&lt;' and char != '&gt;'):
                break

    # if the stack is not empty, the line is corrupted, so we can skip it
    if stack:
        continue

    # if we've reached this point, the line is not corrupted, so we can add the appropriate score
    if char == ')':
        score += 3
    elif char == ']':
        score += 57
    elif char == '}':
        score += 1197
    elif char == '&gt;':
        score += 25137

# print the final score
print(score)