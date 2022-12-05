"""You can solve this problem by keeping track of the current score, and the score of the highest-scoring corrupted line. To do this, you can use a stack to keep track of the currently open chunks. Whenever you encounter an opening character, you can push it onto the stack. Whenever you encounter a closing character, you can pop the last opening character from the stack and check if it matches the closing character. If it does not match, then the line is corrupted and you can update the current and highest-scoring corrupted line scores accordingly. Here is some sample code that you can use to solve this problem:

"""
# Read input from file
with open('10_input', 'r') as f:
  lines = f.readlines()

# Initialize scores
current_score = 0
highest_score = 0

# Loop over lines
for line in lines:
  # Initialize stack
  stack = []

  # Loop over characters in line
  for c in line:
    # Check for opening characters
    if c in '([{<':
      stack.append(c)

    # Check for closing characters
    elif c in ')]}>':
      # Check if stack is empty
      if not stack:
        # Update scores
        current_score = 3 if c == ')' else 57 if c == ']' else 1197 if c == '}' else 25137
        highest_score = max(highest_score, current_score)
        break

      # Pop last opening character from stack
      last = stack.pop()

      # Check if opening and closing characters match
      if not ((c == ')' and last == '(') or (c == ']' and last == '[') or (c == '}' and last == '{') or (c == '>' and last == '<')):
        # Update scores
        current_score = 3 if c == ')' else 57 if c == ']' else 1197 if c == '}' else 25137
        highest_score = max(highest_score, current_score)
        break

# Print highest score
print(highest_score)
"""

You can then run this code by saving it to a file and running it with the python interpreter, like this:

"""
python solution.py
"""

This should print the highest-scoring corrupted line to the console."""