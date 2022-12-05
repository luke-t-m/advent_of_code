"""First, let's define a function `move_crate` that takes as input the initial state of the stacks of crates, the source stack, the destination stack, and the number of crates to move. This function should return the new state of the stacks of crates after moving the specified number of crates from the source stack to the destination stack.

Next, we'll define a function `process_instructions` that takes as input the initial state of the stacks of crates and a list of instructions. This function will iterate through the instructions and call the `move_crate` function to update the state of the stacks of crates after each instruction.

Finally, we'll define a function `get_top_crates` that takes as input the final state of the stacks of crates and returns a string containing the top crate of each stack concatenated together.

Here is the code:

"""
# Define the move_crate function
def move_crate(stacks, source_stack, dest_stack, num_crates):
  # Get the source and destination stacks
  source = stacks[source_stack]
  dest = stacks[dest_stack]
  
  # Move the specified number of crates from the source stack to the destination stack
  moved_crates = source[-num_crates:]
  source = source[:-num_crates]
  dest = dest + moved_crates
  
  # Update the stacks with the new state
  stacks[source_stack] = source
  stacks[dest_stack] = dest
  
  return stacks

# Define the process_instructions function
def process_instructions(stacks, instructions):
  # Iterate through the instructions
  for instruction in instructions:
    # Parse the instruction
    tokens = instruction.split()
    num_crates = int(tokens[1])
    source_stack = int(tokens[2])
    dest_stack = int(tokens[5])
    
    # Move the specified number of crates from the source stack to the destination stack
    stacks = move_crate(stacks, source_stack, dest_stack, num_crates)
  
  return stacks

# Define the get_top_crates function
def get_top_crates(stacks):
  # Get the top crate of each stack
  top_crates = [stack[-1] for stack in stacks]
  
  # Return the concatenated string of top crates
  return ''.join(top_crates)

# Read the input from the file 5_input
with open('5_input', 'r') as f:
  input_lines = f.read().strip().split('\n')

# Parse the input
stacks = []
instructions = []
for line in input_lines:
  if '[' in line:
    # This line contains the initial state of the stacks of crates
    # Parse the line to get the crates in each stack
    stacks = [[crate for crate in stack if crate != ' '] for stack in line.split(']') if stack]
  else:
    # This line contains an instruction
    instructions.append(line)

# Process the instructions to get the final state of the stacks of crates
stacks = process_instructions(stacks, instructions)

# Get the top crates of"""