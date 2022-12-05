"""To solve this problem, you can use a stack to keep track of the opening and closing characters in the input. As you read the input, you can push each opening character onto the stack. If you encounter a closing character, you can pop the last opening character from the stack and check if the pair of characters is valid. If the pair is not valid, then the line is corrupted and you can stop processing the line and move on to the next line. Here is a possible solution in Python:

"""
# Open the input file
with open("10_input", "r") as f:
    # Read each line in the file
    for line in f:
        # Initialize an empty stack
        stack = []
        
        # Initialize a variable to keep track of the score for this line
        score = 0
        
        # Initialize a variable to keep track of whether the line is corrupted
        corrupted = False
        
        # Read each character in the line
        for c in line:
            # If the character is an opening character, push it onto the stack
            if c in ["(", "[", "{", "<"]:
                stack.append(c)
            # If the character is a closing character, pop the last opening character from the stack
            # and check if the pair of characters is valid
            elif c in [")", "]", "}", ">"]:
                # If the stack is empty, then this line is corrupted
                if not stack:
                    corrupted = True
                    break
                # Pop the last opening character from the stack
                last_opening = stack.pop()
                # Check if the pair of characters is valid
                if (last_opening == "(" and c != ")") or (last_opening == "[" and c != "]") or (last_opening == "{" and c != "}") or (last_opening == "<" and c != ">"):
                    corrupted = True
                    break
        
        # If the stack is not empty, then this line is corrupted
        if stack:
            corrupted = True
        
        # If the line is not corrupted, calculate the score for this line
        if not corrupted:
            # If the line is not corrupted, then the score for the line is the sum of the scores for each illegal character on the line
            for c in line:
                if c == ")":
                    score += 3
                elif c == "]":
                    score += 57
                elif c == "}":
                    score += 1197
                elif c == ">":
                    score += 25137
        
        # Print the score for this line
        print(score)
""""""