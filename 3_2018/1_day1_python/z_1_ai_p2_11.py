"""First, we will write a function to read the input from the file "1_input". Then we will use that function to read the input into a list of integers. Next, we will initialize a set to keep track of the frequencies we have seen so far and a variable to keep track of the current frequency. We will then loop through the list of integers, adding each number to the current frequency and checking if the resulting frequency is in our set of frequencies we have seen. If it is, we will return the frequency and exit the loop. If we reach the end of the list without finding a duplicate frequency, we will go back to the start of the list and repeat this process until we find the first duplicate frequency. Here is the implementation in python:

"""
def read_input():
    with open("1_input") as f:
        return [int(x) for x in f.read().splitlines()]


def first_duplicate_frequency(changes):
    seen_frequencies = set()
    current_frequency = 0
    while True:
        for change in changes:
            current_frequency += change
            if current_frequency in seen_frequencies:
                return current_frequency
            seen_frequencies.add(current_frequency)

changes = read_input()
result = first_duplicate_frequency(changes)
print(result)
""""""