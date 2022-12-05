"""Here is a solution in Python:

"""
# Open the input file
with open('10_input', 'r') as f:
  # Read the input lines
  lines = f.readlines()
print(lines)
# Initialize the total score
total_score = 0

# Loop over the lines
for line in lines:
  # Initialize the current score and stack
  current_score = 0
  stack = []

  # Loop over the line's characters
  for c in line:
    # If the character is an opening bracket, add it to the stack
    if c in '([{<':
      stack.append(c)

    # If the character is a closing bracket, pop the last character from the stack
    elif c in ')]}>':
      last_bracket = stack.pop()

      # If the character is not the expected closing bracket for the last opening bracket,
      # add the error score and break
      if (c == ')' and last_bracket != '(') or (c == ']' and last_bracket != '[') or \
         (c == '}' and last_bracket != '{') or (c == '>' and last_bracket != '<'):
        current_score += ord(c)
        break

  # If the stack is empty, the line is correct, so add the current score to the total score
  if not stack:
    total_score += current_score

# Print the total score
print(total_score)
""""""