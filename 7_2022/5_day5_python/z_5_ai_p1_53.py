"""The following code should correctly solve the problem described above:

"""
def move_crate(stacks, a, b):
  # remove top crate from stack a and append it to stack b
  stacks[b].append(stacks[a].pop())

# read input from file
with open('5_input', 'r') as f:
  lines = f.readlines()

# parse input
stacks = [[] for _ in range(3)]
for line in lines:
  if line[0] == '[':
    # line is a stack
    for c in line.strip():
      if c.isalpha():
        # add crate to the correct stack
        stacks[len(stacks[0])].append(c)
  elif 'move' in line:
    # line is a move command
    a, b = map(int, line.split()[-2:])
    move_crate(stacks, a-1, b-1)

# combine top crates from all stacks
result = ''.join(stack[-1] for stack in stacks)
print(result)
""""""