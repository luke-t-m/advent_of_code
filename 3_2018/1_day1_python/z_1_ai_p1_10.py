"""Here's the code:
"""
with open('1_input') as input_file:
    frequencies = [int(line.strip()) for line in input_file]

print(sum(frequencies))
"""

To run this code, create a file called `1_input` in the same directory as the code, and put each frequency change on a separate line. Then, run the code using `python`."""