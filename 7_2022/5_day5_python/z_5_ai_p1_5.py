"""The first step is to read the input from a file.

"""python
with open("5_input", "r") as file:
    data = file.readlines()
"""

Next, we can split the input string into the initial arrangement of crates and the rearrangement procedure.

"""python
init = data[0].strip().split("\n")
procedure = data[1:]
"""

We can then convert the initial arrangement of crates into a list of lists.

"""python
init = [list(stack) for stack in init]
"""

We can then define a function that takes in a list of lists representing the arrangement of crates, and a string representing a step in the rearrangement procedure, and returns a new list of lists representing the updated arrangement of crates.

"""python
def move_crate(crate_arrangement, step):
    # Split the step into its component parts.
    # The first number represents the number of crates to move.
    # The second and third numbers represent the source and destination stacks.
    num_crates, source, dest = map(int, step.split())

    # Move the top num_crates crates from the source stack to the destination stack.
    crates = crate_arrangement[source - 1][:num_crates]
    crate_arrangement[source - 1] = crate_arrangement[source - 1][num_crates:]
    crate_arrangement[dest - 1] = crates + crate_arrangement[dest - 1]

    return crate_arrangement
"""

We can then loop through the rearrangement procedure, applying the `move_crate` function to the arrangement of crates at each step.

"""python
for step in procedure:
    init = move_crate(init, step)
"""

Finally, we can print the top crate from each stack by looping through the arrangement of crates and printing the first character from each stack.

"""python
result = ""
for stack in init:
    result += stack[0]
print(result)
"""

Putting it all together, we have the following code:

"""python
with open("5_input", "r") as file:
    data = file.readlines()

init = data[0].strip().split("\n")
procedure = data[1:]

init = [list(stack) for stack in init]

def move_crate(crate_arrangement, step):
    num_crates, source, dest = map(int, step.split())

    crates = crate_arrangement[source - 1][:num_crates]
    crate_arrangement[source - 1] = crate_arrangement[source - 1][num_crates:]
    crate_arrangement[dest - 1] = crates + crate_arrangement[dest - 1]

    return crate_arrangement

for step in procedure:
    init = move_crate(init, step)

result = ""
for stack in init:
    result += stack[0]
print(result)
""""""