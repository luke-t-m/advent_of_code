"""The first step is to read the frequency changes from the file "1_input". We can do that using the `open` and `readlines` functions:

"""
with open("1_input") as f:
    lines = f.readlines()
"""

`lines` will be a list of strings, with each string representing a frequency change. To get the resulting frequency, we need to sum all the changes. We can use a for loop to iterate over the lines and sum the values:

"""
resulting_frequency = 0

for line in lines:
    resulting_frequency += int(line)

print(resulting_frequency)
"""

Putting it all together, we have:

"""
with open("1_input") as f:
    lines = f.readlines()

resulting_frequency = 0

for line in lines:
    resulting_frequency += int(line)

print(resulting_frequency)
""""""