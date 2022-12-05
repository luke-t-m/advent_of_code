"""First, we need to read the input file. We'll use the `with open()` syntax to open the file and read its contents.

"""
with open('5_input') as f:
  input_data = f.read()
"""

Next, we'll split the input into lines using the `.split()` method, and then split each line on the `' from '` and `' to '` substrings to extract the stack numbers and the number of crates being moved.

"""
input_lines = input_data.strip().split('\n')
moves = []
for line in input_lines:
  move_parts = line.split(' from ')
  n_crates = int(move_parts[0])
  from_stack, to_stack = map(int, move_parts[1].split(' to '))
  moves.append((n_crates, from_stack, to_stack))
"""

Next, we'll create a `stacks` list that represents the initial state of the stacks, where each element of the list is a stack represented as a list of strings (the crate labels). We'll also create a `top_crates` list that will store the top crate of each stack at each step of the rearrangement.

"""
stacks = []
top_crates = []
for line in input_lines:
  # if the line is a crate label, add it to the top of the corresponding stack
  if len(line) == 1:
    stacks[-1].append(line)
  # if the line is a move, add an empty list to the stacks list to represent the new stack
  else:
    stacks.append([])
    top_crates.append(None)
"""

Now we can loop through the `moves` list and apply each move to the `stacks` list.

"""
for move in moves:
  n_crates, from_stack, to_stack = move
  # remove the top `n_crates` crates from the `from_stack` and add them to the `to_stack`
  for _ in range(n_crates):
    crate = stacks[from_stack - 1].pop()
    stacks[to_stack - 1].append(crate)
  # update the top_crates list with the new top crate of each stack
  for i, stack in enumerate(stacks):
    top_crates[i] = stack[-1] if stack else None
"""

Finally, we can join the elements of the `top_crates` list to create the message the Elves are looking for and print it.

"""
message = ''.join(top_crates)
print(message)
"""

Here's the complete code:

"""
with open('5_input') as f:
  input_data = f.read()

input_lines = input_data.strip().split('\n')
moves = []
for line in input_lines:
  move_parts = line.split(' from ')
  n_crates = int(move_parts[0])
  from_stack, to_stack = map(int, move_parts[1].split(' to '))
  moves.append((n_crates, from_stack, to_stack"""