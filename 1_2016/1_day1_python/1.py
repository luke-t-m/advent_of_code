import re

f = open("input","r")
lines = f.readlines()[0]

turns = re.findall("\D\d\d?\d?\d?", lines)
turns = list(map(lambda x: [x[:1], int(x[1:])], turns))

ds = [(0,1), (1,0), (0,-1), (-1, 0)]

# do without storing previously visited positions
def follow_turns(turns, run_till = None, rxy = None, rpxy = None):
    x, y, di = 0, 0, 0
    first_repeat = None
    for c, v in enumerate(turns):
        if run_till != None and c >= run_till: return
        di = (di + (2 * int(v[0] == "L") - 1)) % 4
        px, py = x, y
        x, y = x + v[1] * ds[di][0], y + v[1] * ds[di][1]
        if rpxy != None:
            if x == px and rxy[1] == rpxy[1]: wx, wy, t1, t2 = x, rxy[1], (rxy[0], rpxy[0]), (y, py)
            elif y == py and rxy[0] == rpxy[0]: wx, wy, t1, t2 = rxy[0], y, (x, px), (rxy[1], rpxy[1])
            else: continue
            if wx >= min(t1) and wx <= max(t1) and wy >= min(t2) and wy <= max(t2): return (wx, wy)
        elif first_repeat == None: first_repeat = follow_turns(turns, c-1, (x, y), (px, py))      
    return (abs(x) + abs(y), abs(first_repeat[0]) + abs(first_repeat[1]))

answers = follow_turns(turns)
print(f"Problem 1: {answers[0]}\nProblem 2: {answers[1]}")