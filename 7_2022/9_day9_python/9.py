#!/usr/bin/env python3.10

input = open("9_input").readlines()

dirs = {"U":(0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)}

def solve(input, no_knots):
    visited = set()
    knots = [[0,0] for x in range(no_knots)]
    for instr in input:
        instr = instr.strip().split(" ")
        n, d = int(instr[1]), dirs[instr[0]]
        for i in range(n):
            knots[0][0] += d[0]
            knots[0][1] += d[1]
            for k in range(1, len(knots)):
                dx, dy = 0, 0
                match (knots[k-1][0] - knots[k][0], knots[k-1][1] - knots[k][1]):
                    case (2, 0): dx = 1
                    case (-2, 0): dx = -1
                    case (0, 2): dy = 1
                    case (0, -2): dy = -1
                    case (2, 1) | (1, 2) | (2, 2): dx, dy = 1, 1
                    case (-2, 1) | (-1, 2) | (-2, 2): dx, dy = -1, 1
                    case (2, -1) | (1, -2) | (2, -2): dx, dy = 1, -1
                    case (-2, -1) | (-1, -2)| (-2, -2): dx, dy = -1, -1
                knots[k][0] += dx
                knots[k][1] += dy
            visited.add((knots[-1][0], knots[-1][1]))
    return len(visited)

print(f"Part one: {solve(input, 2)}\nPart two: {solve(input, 10)}")
