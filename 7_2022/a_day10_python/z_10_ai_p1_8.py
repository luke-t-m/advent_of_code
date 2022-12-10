"""The following code will solve the problem:

"""
with open('10_input') as f:
  instructions = f.read().strip().split('\n')

x = 1
signal_strengths = []
for i, instruction in enumerate(instructions):
  if instruction.startswith('addx'):
    x += int(instruction.split()[1])
  if (i+1) % 40 == 20:
    signal_strengths.append(x * (i+1))

print(sum(signal_strengths))
"""

This code first reads the instructions from the file `10_input` and stores them in a list. It then initializes the `x` register to `1`, which is its initial value. The code then iterates through the instructions, executing each one by either adding the specified value to `x` or doing nothing if the instruction is `noop`. As it iterates through the instructions, the code checks whether the current cycle is the 20th, 60th, 100th, 140th, 180th, or 220th cycle (i.e., if the current cycle is a multiple of 40, with 20 added to it). If it is, the code adds the product of the current value of `x` and the current cycle number to a list of signal strengths. Finally, the code prints the sum of the signal strengths."""