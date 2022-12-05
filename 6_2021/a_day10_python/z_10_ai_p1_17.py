"""You can solve this problem by using a stack. The stack will be used to store the opening brackets as they are encountered. When a closing bracket is encountered, it is checked against the top element of the stack. If the closing bracket does not match the top element of the stack, the line is corrupted and the score for the line can be calculated by looking up the closing bracket in the table provided in the prompt.

Here is an example solution in Python:

"""
BRACKETS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def syntax_error_score(line):
    stack = []
    score = 0
    for ch in line:
        if ch in BRACKETS:
            if not stack or BRACKETS[ch] != stack[-1]:
                score += BRACKETS[ch]
                break
            stack.pop()
        else:
            stack.append(ch)
    return score

with open("10_input", "r") as f:
    for line in f:
        print(syntax_error_score(line))
""""""