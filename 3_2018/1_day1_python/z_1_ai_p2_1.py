"""The problem can be solved by keeping track of the current frequency and adding the frequency changes one by one. We can use a while loop to iterate over the frequency changes. Inside the while loop, we can use a set to keep track of the frequencies that have been reached so far. If we reach a frequency that has already been seen, we can stop the loop and print the frequency.

Here is the code:

"""
# Read the input from the file
with open('1_input') as f:
    changes = [int(x) for x in f]

# Start at frequency 0
current_freq = 0

# Keep track of the frequencies that have been reached so far
seen = set()

# Iterate over the frequency changes
while True:
    for change in changes:
        # Update the current frequency
        current_freq += change
        
        # If the current frequency has been seen before, print it and stop the loop
        if current_freq in seen:
            print(current_freq)
            break
        
        # Otherwise, add the current frequency to the set of seen frequencies
        seen.add(current_freq)
"""

To run this code, save it to a file called `1.py` and run it using `python 1.py`. It will print the first frequency that is reached twice."""