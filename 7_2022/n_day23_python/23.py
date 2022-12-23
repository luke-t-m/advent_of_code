#!/usr/bin/env python3

def none_in(list, set):
    for el in list:
        if el in set: return False
    return True

    

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)] #NSEW

all_diags = []
for xm in [-1, 0, 1]:
    for ym in [-1, 0, 1]:
        if xm != 0 or ym != 0: all_diags.append((xm, ym))





input = open("23_input").readlines()
#input = open("23_test").readlines()
#input = open("23_test_2").readlines()


elves = set()
for iy, r in enumerate(input):
    for ix, el in enumerate(r):
        if el == "#": elves.add((ix, iy))

round = 0
while True:
    round += 1
    #print(elves, len(elves))
    if round % 100 == 0: print(round)
    next_elves = set()
    attempted_moves = set()
    blacklist = set()
    for elf in elves:
        x, y = elf
        for xm, ym in all_diags:
            if (x+xm, y+ym) in elves: break
        else:
            next_elves.add(elf)
            continue
        for xm, ym in dirs:
            pos_elf = x+xm, y+ym
            if ((xm and none_in([(x+xm, y-1), (x+xm, y), (x+xm, y+1)], elves))
             or (ym and none_in([(x-1, y+ym), (x, y+ym), (x+1, y+ym)], elves))):
                if pos_elf in attempted_moves: blacklist.add(pos_elf)
                else: attempted_moves.add(pos_elf)
                break
    for elf in elves:
        x, y = elf
        for xm, ym in all_diags:
            if (x+xm, y+ym) in elves: break
        else:
            continue
        for xm, ym in dirs:
            pos_elf = x+xm, y+ym
            if ((xm and none_in([(x+xm, y-1), (x+xm, y), (x+xm, y+1)], elves))
             or (ym and none_in([(x-1, y+ym), (x, y+ym), (x+1, y+ym)], elves))):
                if pos_elf in blacklist: next_elves.add(elf)
                else: next_elves.add(pos_elf)
                break
        else: next_elves.add(elf)
    first_dir = dirs.pop(0)
    dirs.append(first_dir) 
    if next_elves == elves: break      
    elves = next_elves

print(round) # part two
minx, maxx, miny, maxy = 0, 0, 0, 0
for x, y in elves:
    minx = min(x, minx)
    maxx = max(x, maxx)
    miny = min(y, miny)
    maxy = max(y, maxy)

print(minx, maxx, miny, maxy)
area = (maxx - minx + 1) * (maxy - miny + 1)

print(area - len(elves))
# 3953 low