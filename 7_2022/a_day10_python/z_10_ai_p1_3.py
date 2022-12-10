"""The code below will solve the problem as described above.

"""
x = 1

signal_strengths = []

# Read input from file 10_input
with open("10_input", "r") as f:
    for line in f:
        # Split line by whitespace
        line = line.split()
        
        # Parse instruction and value
        instr = line[0]
        val = int(line[1])
        
        # Execute instruction
        if instr == "addx":
            x += val
        elif instr == "noop":
            pass
        
        # Check if current cycle is a multiple of 20 or 40
        if cycle % 20 == 0 or cycle % 40 == 0:
            signal_strengths.append(cycle * x)

# Print the sum of the signal strengths
print(sum(signal_strengths))
""""""