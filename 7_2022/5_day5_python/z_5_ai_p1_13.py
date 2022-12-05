"""The first thing that we need to do is read in the input from the file named `5_input`. We can do this by opening the file and reading its contents into a variable.

"""
with open('5_input') as f:
  data = f.read()
"""

Next, we need to parse the input data to extract the information about the starting configuration of the crates and the sequence of moves to be performed. We can do this by splitting the input string on the newline character and then iterating over the resulting list of strings.

"""
lines = data.split('\n')
stacks = []
moves = []

for line in lines:
  # Extract the starting configuration of the crates
  if line[0] == '[':
    # Parse the line to extract the crates in the stack
    crates = line.strip('[]').split(' ')
    stacks.append(crates)
  # Extract the sequence of moves
  else:
    # Parse the line to extract the details of the move
    move = line.split(' ')
    moves.append(move)
"""

Now that we have extracted the information about the starting configuration of the crates and the sequence of moves, we can simulate the rearrangement procedure. We can do this by iterating over the list of moves and performing each move in sequence.

"""
for move in moves:
  # Get the source and destination stacks
  src_stack = int(move[1]) - 1
  dest_stack = int(move[3]) - 1
  # Get the number of crates to be moved
  num_crates = int(move[2])
  # Move the crates from the source stack to the destination stack
  for i in range(num_crates):
    # Remove the top crate from the source stack and add it to the destination stack
    crate = stacks[src_stack].pop()
    stacks[dest_stack].append(crate)
"""

Finally, we can output the top crate from each stack by iterating over the `stacks` list and printing the top crate from each stack.

"""
for stack in stacks:
  print(stack[-1], end='')
"""

Putting it all together, we get the following solution:

"""
with open('5_input') as f:
  data = f.read()

lines = data.split('\n')
stacks = []
moves = []

for line in lines:
  # Extract the starting configuration of the crates
  if line[0] == '[':
    # Parse the line to extract the crates in the stack
    crates = line.strip('[]').split(' ')
    stacks.append(crates)
  # Extract the sequence of moves
  else:
    # Parse the line to extract the details of the move
    move = line.split(' ')
    moves.append(move)

# Simulate the rearrangement procedure
for move in moves:
  # Get the source and destination stacks
  src_stack = int(move[1]) - 1
  dest_stack = int(move[3]) - 1
  # Get the number of crates to be moved
  num_crates = int(move[2])
  # Move the crates from the source stack to the destination stack
  for i in"""