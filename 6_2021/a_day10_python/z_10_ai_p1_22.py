"""The following code will solve the problem correctly in python and print the answer.

"""
# Read input from file
with open("10_input") as input_file:
    lines = input_file.read().splitlines()

# Initialize score and corrupted_lines
score = 0
corrupted_lines = []

# Loop through lines
for line in lines:
    # Initialize stack and line_score
    stack = []
    line_score = 0
    
    # Loop through characters in line
    for ch in line:
        # Push opening characters to stack
        if ch in "([{<":
            stack.append(ch)
        
        # Check closing characters
        elif ch in ")]}>":
            # If stack is empty, line is corrupted
            if not stack:
                corrupted_lines.append(line)
                break
            
            # If closing character does not match last opening character on stack, line is corrupted
            if (ch == ")" and stack[-1] != "(") or (ch == "]" and stack[-1] != "[") or (ch == "}" and stack[-1] != "{") or (ch == ">" and stack[-1] != "<"):
                corrupted_lines.append(line)
                break
            
            # If closing character matches last opening character on stack, pop opening character from stack and add to score
            else:
                stack.pop()
                if ch == ")":
                    line_score += 3
                elif ch == "]":
                    line_score += 57
                elif ch == "}":
                    line_score += 1197
                elif ch == ">":
                    line_score += 25137
    
    # If stack is not empty, line is corrupted
    if stack:
        corrupted_lines.append(line)
    
    # Add line score to total score
    score += line_score

# Print score and corrupted lines
print(score)
print(corrupted_lines)
""""""