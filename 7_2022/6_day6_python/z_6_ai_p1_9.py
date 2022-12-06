"""The problem can be solved as follows:

1. Read the input from the file `6_input`
2. Initialize a counter `count` to 0
3. Iterate over the characters in the input, updating the counter for each character
4. When the last four characters are all different, print the counter and exit

Here is the solution in Python:

"""
with open('6_input', 'r') as f:
  input = f.read()

count = 0
for i in range(len(input)):
  count += 1
  if len(set(input[i:i+4])) == 4:
    print(count)
    break
""""""