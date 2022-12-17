#!/usr/bin/env python3
from copy import deepcopy
import math

hold_grid = 30

def move(grid, dir):
    match dir:
        case "^": xscan, yscan, xmod, ymod = 1, -1, 0, -1
        case ">": xscan, yscan, xmod, ymod = -1, 1, 1, 0
        case "<": xscan, yscan, xmod, ymod = 1, 1, -1, 0
    cgrid = deepcopy(grid)
    break_in = math.inf
    for i in range(len(cgrid))[::-yscan]:
        if break_in <= 0: break
        break_in -= 1
        if "@" not in cgrid[i]: continue
        break_in = 3
        for j in range(len(cgrid[i]))[::xscan]:
            if cgrid[i][j] == "@":
                if cgrid[i + ymod][j + xmod] != ".": return False, grid
                cgrid[i + ymod][j + xmod] = "@"
                cgrid[i][j] = "."
    return True, cgrid

def solidify(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@": grid[i][j] = "#"
    return grid

def rocks_fall_everybody_dies(input, n, memorise = False):
    wind = input.strip()
    grid = [["|"] + 7 * ["#"] + ["|"]]
    memory = {0: (0, 0)}

    rock, shape_i, wind_i, height = 0, 0, 0, hold_grid - 1
    while rock < n:
        if rock % 100 == 0: print(f"{rock} / {n}, {len(grid)}, {height}, {100 * rock / n} %", end = "\r")
        for ign in range(3):
            grid.append(["|"] + 7 * ["."] + ["|"])
        for l in shapes[shape_i].split("\n"):
            grid.append(list("|.." + l + "." * (5 - len(l)) + "|"))
        shape_i = (shape_i + 1) % len(shapes)

        moved = True
        while moved:
            ignored, grid = move(grid, wind[wind_i])
            moved, grid = move(grid, "^")
            wind_i = (wind_i + 1) % len(wind)
            
        grid = solidify(grid)
        for x in range(len(grid))[::-1]:
            if grid[x] != clear_layer:
                grid = grid[:x+1]
                break

        l = len(grid) - hold_grid
        if l >= 0:
            height += l
            grid = grid[l:]

        if memorise and "." not in grid[-1]:
            if wind_i in memory:
                prev_rock, prev_height = memory[wind_i]
                print(f"{rock} / {n}, {len(grid)}, {height}, {100 * rock / n} %")
                print(f"PREV FULL ROW wind index: {wind_i}, rock: {rock}, prev_rock: {prev_rock}, height: {height}, prev_height: {prev_height}")
                
                subjump = rock - prev_rock
                to_jump = n - rock
                jumps = to_jump // subjump
                rock += jumps * subjump
                height += (height - prev_height) * jumps - 1
                memorise = False
                continue
            else:
                print(f"{rock} / {n}, {len(grid)}, {height}, {100 * rock / n} %")
                print(f"ADDED FULL ROW wind_index: {wind_i}, rock: {rock}, height: {height}")

                memory[wind_i] = (rock, height)
        rock += 1
    print()
    return height


input = open("17_input").read()

shapes = ["@@@@", ".@.\n@@@\n.@.", "@@@\n..@\n..@", "@\n@\n@\n@", "@@\n@@"]
clear_layer = ["|"] + 7 * ["."] + ["|"]

print(f"Part one: {rocks_fall_everybody_dies(input, 2022)}")
print(f"Part two: {rocks_fall_everybody_dies(input, 1000000000000, memorise = True)}")