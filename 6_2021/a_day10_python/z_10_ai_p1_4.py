"""Here is a solution in Python:

"""
# Read input from file called 10_input
with open("10_input", "r") as file:
    lines = file.readlines()

# Parse the input to find the corrupted lines
corrupted_lines = []
for line in lines:
    stack = []
    for c in line:
        if c in ["(", "[", "{", "&lt;"]:
            stack.append(c)
        elif c in [")", "]", "}", "&gt;"]:
            if not stack:
                corrupted_lines.append(line)
                break
            last_chunk = stack.pop()
            if (last_chunk == "(" and c != ")") or (last_chunk == "[" and c != "]") or (last_chunk == "{" and c != "}") or (last_chunk == "&lt;" and c != "&gt;"):
                corrupted_lines.append(line)
                break

# Calculate the syntax error score for each corrupted line
score = 0
for line in corrupted_lines:
    first_error_char = line[line.index("(") + 1:].index(")")
    if first_error_char == ")":
        score += 3
    elif first_error_char == "]":
        score += 57
    elif first_error_char == "}":
        score += 1197
    elif first_error_char == "&gt;":
        score += 25137

# Print the final score
print(score)
""""""