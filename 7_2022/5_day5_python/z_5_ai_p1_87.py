"""Here is the code to solve the problem:
"""
# read the inputs
with open('5_input') as f:
    lines = f.readlines()

#parse the inputs into list of tuples (n, x, y) where 
#n is the number of crates to move from x to y
moves = []
for line in lines:
    n, x, _, y = line.split()
    moves.append((int(n), int(x), int(y)))

#initialize the stacks of crates
stacks = [['Z'], ['M'], ['P']]

#perform the moves
for move in moves:
    n, x, y = move
    #move the crates one by one
    for i in range(n):
        stacks[y-1].append(stacks[x-1].pop())

#print the top crates of each stack
for stack in stacks:
    print(stack[-1], end='')
"""
The output of this code is the answer to the problem."""