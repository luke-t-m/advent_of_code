"""The following code can be used to solve this problem. It reads the input from a file named 10_input, parses the instructions, and simulates the CPU by executing each instruction. It then calculates the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles, as specified in the problem, and prints the result.

"""
with open("10_input") as f:
  instructions = [line.strip() for line in f]

x = 1
for i, instruction in enumerate(instructions):
  if instruction.startswith("noop"):
    pass
  elif instruction.startswith("addx"):
    v = int(instruction.split()[1])
    x += v
  else:
    raise ValueError("Invalid instruction: {}".format(instruction))

  if i + 1 in (20, 60, 100, 140, 180, 220):
    print(i + 1, x)
""""""