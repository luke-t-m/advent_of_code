# read from input file
with open("6_input") as f:
    buffer = f.read()

# initialize variables
start = -1
prev = ""

# loop through buffer characters
for i, c in enumerate(buffer):
    if prev != "":
        if c not in prev:
            if len(prev) == 3:
                start = i
                break
            else:
                prev += c
        else:
            prev = c
    else:
        prev = c

# print result
print(start)