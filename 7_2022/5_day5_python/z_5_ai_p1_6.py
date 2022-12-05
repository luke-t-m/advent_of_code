# First, let's parse the input
def parse_input(input_str: str):
    lines = input_str[:4].strip().split('\n')
    initial_configuration = lines[:-1]
    moves = []
    lines = input_str.strip().split('\n')
    for move in lines[-1:]:
        from_stack, to_stack = move.split(' from ')[0], move.split(' from ')[1]
        from_stack = int(from_stack.split(" ")[1])
        to_stack = int(to_stack.split("to ")[1])
        moves.append((from_stack, to_stack))
    return initial_configuration, moves

# Then, let's define a function that applies a move to the current configuration
def apply_move(configuration, move):
    from_stack, to_stack = move[0], move[1]
    # remove the top crate from the from_stack
    top_crate = str(list(configuration[from_stack]).pop(0))
    configuration[from_stack] = configuration[from_stack][1:]
    # add the crate to the to_stack
    configuration[to_stack] += top_crate
    print(configuration)
    return configuration

# Now let's define a function that applies all the moves to the initial configuration
def apply_moves(initial_configuration, moves):
    configuration = initial_configuration[:]
    for move in moves:
        configuration = apply_move(configuration, move)
    return configuration

# Finally, let's define the main function that parses the input and prints the final configuration
def main(input_str: str):
    initial_configuration, moves = parse_input(input_str)
    final_configuration = apply_moves(initial_configuration, moves)
    print(''.join(final_configuration))

# Let's test the main function with the example given in the prompt
input_str = """
[D]    
[N] [C]    
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

input_str = open("5_test").read()

main(input_str)
# This should print "CMZ""""