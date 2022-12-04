"""To solve this problem, we need to read in the input from the file 1_input and process it to find the resulting frequency. We can do this using a few lines of Python code.

First, we'll open the input file and read in each line as a string. Then, we'll convert each string to an integer and add it to a running total. Finally, we'll print the total. Here's the code:

with open('1_input') as f:
    lines = f.readlines()

total = 0
for line in lines:
    total += int(line)

print(total)"""