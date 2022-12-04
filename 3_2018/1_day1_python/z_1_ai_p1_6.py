# Open the input file, read the frequencies and sum them
f = open("1_input", "r")
frequencies = f.readlines()
f.close()

# Convert the list of strings to a list of integers
frequencies = [int(x) for x in frequencies]

# Sum the frequencies
result = sum(frequencies)

# Print the result
print(result)