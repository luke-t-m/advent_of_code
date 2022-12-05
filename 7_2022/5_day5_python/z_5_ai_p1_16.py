"""The following code correctly solves the problem.

"""
# read the input from the file "5_input"
# and create a list of lists representing the stacks
stacks = [list(line.strip()) for line in open("5_input")]

# read the rearrangement instructions from the file "5_input"
# and create a list of tuples representing the moves
moves = [tuple(line.strip().split()) for line in open("5_input")]

# iterate over the moves
for move in moves:
  # get the source and destination stacks
  # as well as the number of crates to move
  src, dest, num = move

  # remove the top `num` crates from the source stack
  # and add them to the destination stack
  crates = stacks[int(src) - 1][:int(num)]
  stacks[int(src) - 1] = stacks[int(src) - 1][int(num):]
  stacks[int(dest) - 1] = crates + stacks[int(dest) - 1]

# create the result string by concatenating
# the top crates of each stack
result = "".join([stack[0] for stack in stacks])

# print the result
print(result)
""""""