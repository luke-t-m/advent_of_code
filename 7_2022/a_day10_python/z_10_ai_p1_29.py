"""To solve this problem in Python, you can create a function that takes the input program as a parameter and simulates the CPU's execution of the program. The function should return the values of the X register at the 20th, 60th, 100th, 140th, 180th, and 220th cycles.

Here is one way to solve the problem:

"""
def solve(program):
  # Initialize the X register to 1
  x = 1

  # Cycle counter
  c = 0

  # Signal strength history
  history = []

  # Iterate over the instructions in the program
  for instruction in program:
    if instruction.startswith('addx'):
      # Split the instruction to get the value to add to X
      _, value = instruction.split()

      # Convert the value to an integer
      value = int(value)

      # Increment the cycle counter by two, since addx takes two cycles to execute
      c += 2

      # Update the X register by adding the value
      x += value

      # Append the signal strength (cycle number * X register value) to the history
      history.append(c * x)
    else:
      # Increment the cycle counter by one, since noop takes one cycle to execute
      c += 1

  # Return the signal strength at the 20th, 60th, 100th, 140th, 180th, and 220th cycles
  return [history[i] for i in [19, 59, 99, 139, 179, 219]]

# Read the input program from the 10_input file
with open('10_input') as f:
  program = f.read().strip().split('\n')

# Solve the problem and print the answer
print(solve(program))
""""""