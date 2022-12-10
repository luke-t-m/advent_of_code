"""The code to solve the problem is as follows:

"""
# read input from file
with open('10_input', 'r') as f:
  instructions = f.read().strip().split('\n')

# initialize variables
x = 1
signal_strength = 0

# execute instructions
for i, instruction in enumerate(instructions):
  if instruction == 'noop':
    pass
  else:
    value = int(instruction.split()[1])
    x += value
  if (i + 1) % 20 == 0 or (i + 1) % 60 == 0 or (i + 1) % 100 == 0 or (i + 1) % 140 == 0 or (i + 1) % 180 == 0 or (i + 1) % 220 == 0:
    signal_strength += (i + 1) * x

# print answer
print(signal_strength)
"""

Here's an explanation of how the code works:

1. The code reads the instructions from the file `10_input`.
2. It initializes the `x` variable to 1 and the `signal_strength` variable to 0. `x` is the register that stores the value of the X register and `signal_strength` is the variable that stores the signal strength.
3. The code then iterates over the instructions and executes each instruction.
4. If the instruction is `noop`, the code does nothing. Otherwise, the code extracts the value from the instruction and adds it to the `x` variable.
5. After executing an instruction, the code checks if the instruction is the 20th, 60th, 100th, 140th, 180th, or 220th instruction. If it is, the code adds the product of the instruction number and the value of the `x` variable to the `signal_strength` variable.
6. Finally, the code prints the value of the `signal_strength` variable, which is the answer to the problem."""