"""The following code will solve the problem as described above.

"""
# Read in the input file and store the instructions
with open('9_input') as input_file:
    instructions = input_file.read()

# Initialize variables
head_row = 0
head_col = 0
tail_row = 0
tail_col = 0

# Loop through the instructions
for instruction in instructions:
    # Update the position of the head
    if instruction == 'U':
        head_row -= 1
    elif instruction == 'D':
        head_row += 1
    elif instruction == 'L':
        head_col -= 1
    elif instruction == 'R':
        head_col += 1

    # Update the position of the tail
    if (head_row == tail_row and abs(head_col - tail_col) == 1) or (head_col == tail_col and abs(head_row - tail_row) == 1):
        # If the head is adjacent to the tail, move the tail in the same direction as the head
        if instruction == 'U':
            tail_row -= 1
        elif instruction == 'D':
            tail_row += 1
        elif instruction == 'L':
            tail_col -= 1
        elif instruction == 'R':
            tail_col += 1
    elif abs(head_row - tail_row) > 1 or abs(head_col - tail_col) > 1:
        # If the head and tail are not adjacent, move the tail diagonally to keep up with the head
        if instruction == 'U':
            tail_row -= 1
            tail_col -= 1
        elif instruction == 'D':
            tail_row += 1
            tail_col += 1
        elif instruction == 'L':
            tail_row -= 1
            tail_col += 1
        elif instruction == 'R':
            tail_row += 1
            tail_col -= 1

# Print the final position of the tail
print(tail_col, tail_row)
""""""