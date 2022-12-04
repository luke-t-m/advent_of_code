"""The following code will solve the problem. It reads the list of numbers from the file `1_input` and adds them to a set. If a number is already in the set, it prints the number and exits. Otherwise, it continues until the end of the list is reached, then starts over again.

"""
seen = set()
current = 0

with open('1_input') as f:
    for line in f:
        current += int(line.strip())
        if current in seen:
            print(current)
            break
        seen.add(current)
""""""