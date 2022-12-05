"""The following code solves the problem by creating a stack that keeps track of the currently open brackets in the input file. It iterates through each character in each line of the input file and checks if it is an opening bracket. If it is, it pushes the bracket onto the stack. If it is a closing bracket, it pops the top bracket from the stack and checks if the popped bracket is a legal pair with the current closing bracket. If it is not a legal pair, it prints the syntax error score for the line and breaks out of the loop. It repeats this process for each line in the input file.

"""
# Open the input file
with open('10_input', 'r') as f:
    # Read each line in the input file
    for line in f.readlines():
        # Create a stack to keep track of the open brackets
        stack = []
        
        # Iterate through each character in the line
        for c in line:
            # Check if the character is an opening bracket
            if c in ['(', '[', '{', '<']:
                # Push the bracket onto the stack
                stack.append(c)
            # Check if the character is a closing bracket
            elif c in [')', ']', '}', '>']:
                # Pop the top bracket from the stack
                bracket = stack.pop()
                
                # Check if the popped bracket is a legal pair with the current closing bracket
                if (bracket == '(' and c != ')') or (bracket == '[' and c != ']') or (bracket == '{' and c != '}') or (bracket == '<' and c != '>'):
                    # Print the syntax error score for the line
                    if c == ')':
                        print(3)
                    elif c == ']':
                        print(57)
                    elif c == '}':
                        print(1197)
                    elif c == '>':
                        print(25137)
                    
                    # Break out of the loop
                    break
""""""