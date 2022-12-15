#!/usr/bin/env python3
import re


def merge_ranges(ranges):
    ranges.sort()
    index = 0
    for i in range(1, len(ranges)):
        if ranges[index][1] >= ranges[i][0]:
            ranges[index][1] = max(ranges[index][1], ranges[i][1])
        else:
            index += 1
            ranges[index] = ranges[i]
    return ranges[:index+1]

def near_ranges(y, sensbeacs):
    ranges = []
    for s in sensbeacs:
        sx, sy, bx, by = s
        manh = abs(sx - bx) + abs(sy - by)
        to_y = abs(sy - y)
        c = manh - to_y
        if c > 0: ranges.append([sx-abs(c), sx+abs(c)])
    return ranges

def part_one(y, sensbeacs):
    return sum(map(lambda i: i[1] - i[0], merge_ranges(near_ranges(y, sensbeacs))))

def part_two(max_xy, sensbeacs):
    for y in range(max_xy, -1, -1):
        if y % 10000 == 0: print(f"Progress: y = {y}", end='\r')
        cants = merge_ranges(near_ranges(y, sensbeacs))
        if len(cants) > 1:
            assert cants[1][0] - cants[0][1] == 2
            return 4000000 * (cants[0][1] + 1) + y

test = 0

if test:
    input = open("15_test").readlines()
    y, max_xy = 10, 20
else:
    input = open("15_input").readlines()
    y, max_xy = 2000000, 4000000


sensbeacs = []
for line in input:
    r = re.search("Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)", line)
    sensbeacs.append(list(map(int, [r.group(x) for x in range(1,5)])))


print(f"Part one: {part_one(y, sensbeacs)}")
print(f"Part two: {part_two(max_xy, sensbeacs)}")
