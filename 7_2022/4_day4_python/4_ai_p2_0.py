#input = open("4_input").read()
#input = open("4_test").read()
overlap_count = 0
# Open the input file
with open('4_input') as f:
    # Iterate over the lines in the file
    for line in f:
        # Parse the line to extract the range of section IDs for each pair of Elves
        elf1, elf2 = line.strip().split(',')
        elf1_start, elf1_end = map(int, elf1.split('-'))
        elf2_start, elf2_end = map(int, elf2.split('-'))
        # Check if the ranges overlap
        if elf1_start <= elf2_end and elf2_start <= elf1_end:
            # If the ranges overlap, increment the counter
            overlap_count += 1

# Print the number of overlapping assignment pairs
print(overlap_count)
