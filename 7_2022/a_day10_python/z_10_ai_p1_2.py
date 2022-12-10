"""The code below will solve the problem as described.

"""
import sys

def read_input(file):
    with open(file) as f:
        lines = f.read().strip().split('\n')
    return lines

def parse_instruction(instruction):
    parts = instruction.split()
    op = parts[0]
    val = int(parts[1])
    return (op, val)

def execute_instruction(instruction, register):
    op, val = parse_instruction(instruction)
    if op == 'addx':
        register += val
    return register

def compute_signal_strength(program):
    register = 1
    signal_strength = 0
    cycle = 1
    for instruction in program:
        register = execute_instruction(instruction, register)
        if cycle == 20 or cycle % 40 == 0:
            signal_strength += cycle * register
        cycle += 1
    return signal_strength

def main():
    input_file = '10_input'
    program = read_input(input_file)
    signal_strength = compute_signal_strength(program)
    print(signal_strength)

if __name__ == '__main__':
    main()
"""

To run the code, save it to a file called `solution.py` and run `python solution.py` in a terminal. The answer will be printed to the terminal."""