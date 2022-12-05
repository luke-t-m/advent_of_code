"""To solve this problem, you can keep a set of frequencies that you have seen so far, and keep looping over the sequence of changes. Each time you reach a frequency that you have seen before, print it and exit the program. Here is an implementation in Python:

"""
# Read the input
with open("1_input") as f:
    changes = [int(x) for x in f]

# Keep a set of frequencies we have seen so far
seen = set()

# Start at frequency 0
freq = 0

# Keep looping over the changes
while True:
    for change in changes:
        # Update the frequency
        freq += change
        
        # Check if we have seen this frequency before
        if freq in seen:
            # If so, print the frequency and exit
            print(freq)
            exit()

        # Otherwise, add the frequency to the set of seen frequencies
        seen.add(freq)
"""

To run this program, save it in a file called `solution.py` and run it with `python solution.py`. This should print the first frequency that is reached twice."""