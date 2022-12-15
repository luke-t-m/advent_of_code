#!/usr/bin/env python3
import re

def mergeIntervals(arr):
    arr.sort(key=lambda x: x[0])
    index = 0
    for i in range(1, len(arr)):
        if (arr[index][1] >= arr[i][0]):
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]
    return arr[:index+1]

def cant_ranges(y):
    ranges = []
    for s in sensors:
        sx, sy, bx, by = s
        manh = abs(sx - bx) + abs(sy - by)
        to_y = abs(sy - y)
        c = manh - to_y
        if c > 0: ranges.append([sx-abs(c), sx+abs(c)])
    return mergeIntervals(ranges)

def part_one(y):
    return sum(map(lambda i: i[1] - i[0], cant_ranges(y)))

def part_two(max_xy):
    for y in range(max_xy):
        if y % 10000 == 0: print(f"Progress: y = {y}", end='\r')
        cants = cant_ranges(y)
        if len(cants) > 1:
            assert cants[1][0] - cants[0][1] == 2
            return 4000000 * (cants[1][0] + 1) + y

input = open("15_input").readlines()

sensors = []
for line in input:
    r = re.search("Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)", line)
    sensors.append(list(map(int, [r.group(x) for x in range(1,5)])))


print(f"Part one: {part_one(2000000)}")
print(f"Part two: {part_two(4000000)}")
