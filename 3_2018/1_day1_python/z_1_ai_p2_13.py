"""To solve this problem, we first need to read in the input from the file `1_input`. We can do this using the `open` and `readlines` functions in Python.

"""
with open('1_input') as f:
    lines = f.readlines()
"""

Next, we need to parse the input. Each line of the input represents a change in frequency, so we need to convert each line to a number and add it to the current frequency. We can use the `split` method to split each line on the `+` or `-` characters, then convert the resulting string to an integer using the `int` function.

"""
frequency = 0
for line in lines:
    change = int(line.split('+' if '+' in line else '-')[1])
    if '+' in line:
        frequency += change
    else:
        frequency -= change
"""

Now we need to find the first frequency that is reached twice. To do this, we can keep track of all the frequencies we've seen so far in a `set` and check if the current frequency is already in the set. If it is, we've found the first repeated frequency and we can stop the loop.

"""
seen = set()
for line in lines:
    change = int(line.split('+' if '+' in line else '-')[1])
    if '+' in line:
        frequency += change
    else:
        frequency -= change
    if frequency in seen:
        break
    seen.add(frequency)
"""

Finally, we can print the resulting frequency to get the answer to the problem.

"""
print(frequency)
"""

Here is the complete solution:

"""
with open('1_input') as f:
    lines = f.readlines()

frequency = 0
seen = set()
for line in lines:
    change = int(line.split('+' if '+' in line else '-')[1])
    if '+' in line:
        frequency += change
    else:
        frequency -= change
    if frequency in seen:
        break
    seen.add(frequency)

print(frequency)
""""""