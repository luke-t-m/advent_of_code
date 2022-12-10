"""First, we need to read the input from the file `10_input`. We can do this using the `open` function and the `readlines` method:

"""
with open('10_input') as f:
    instructions = f.readlines()
"""

Next, we need to parse these instructions. We can do this by splitting each line on the space character and extracting the instruction and the value. We can store these in a list of tuples, where the first element of each tuple is the instruction and the second element is the value:

"""
parsed_instructions = [(inst.split()[0], int(inst.split()[1])) for inst in instructions]
"""

Now that we have the instructions in a format that we can easily work with, we can simulate the execution of the program. We will need to keep track of the value of the `X` register and the current cycle number. We can do this with two variables:

"""
x = 1
cycle = 1
"""

Next, we will need to iterate over the parsed instructions and execute each one in turn. For the `noop` instruction, we simply increment the cycle number by one. For the `addx` instruction, we increment the cycle number by two and then update the value of `X` by adding the instruction's value. We can do this using a `for` loop:

"""
for inst, val in parsed_instructions:
    if inst == 'noop':
        cycle += 1
    elif inst == 'addx':
        cycle += 2
        x += val
"""

Finally, we need to calculate the signal strength at the 20th cycle and every 40 cycles after that. We can do this using a `while` loop, where we continue looping as long as the current cycle is less than or equal to 220. Inside the loop, we check if the current cycle is the 20th cycle or a multiple of 40, and if so, we calculate the signal strength by multiplying the cycle number by the value of `X` and print it:

"""
while cycle <= 220:
    if cycle == 20 or cycle % 40 == 0:
        signal_strength = cycle * x
        print(signal_strength)
    cycle += 1
"""

Putting all of this together, we get the following code:

"""
with open('10_input') as f:
    instructions = f.readlines()

parsed_instructions = [(inst.split()[0], int(inst.split()[1])) for inst in instructions]

x = 1
cycle = 1

for inst, val in parsed_instructions:
    if inst == 'noop':
        cycle += 1
    elif inst == 'addx':
        cycle += 2
        x += val

while cycle <= 220:
    if cycle == 20 or cycle % 40 == 0:
        signal_strength = cycle * x
        print(signal_strength)
    cycle += 1
""""""