keypad1 =   [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

keypad2 =  [["x", "x", "1", "x", "x"],
            ["x", "2", "3", "4", "x"],
            ["5", "6", "7", "8", "9"],
            ["x", "A", "B", "C", "x"],
            ["x", "x", "D", "x", "x"]]


lines = open("input").readlines()

def traverseKeypad(lines, keypad, start_x, start_y):
    out = ""
    x, y = start_x, start_y
    l = len(keypad)-1
    for line in lines:
        for c in line:
            nx, ny = x, y
            if c == "U": ny = max(0, y-1)
            elif c == "D": ny = min(l, y+1)
            elif c == "L": nx = max(0, x-1)
            elif c == "R": nx = min(l, x+1)
            if keypad[ny][nx] != "x": x, y = nx, ny
        out += str(keypad[y][x])
    return out

print("task 1: " + traverseKeypad(lines, keypad1, 1, 1))
print("task 2: " + traverseKeypad(lines, keypad2, 0, 2))
