#!/usr/bin/env python3

def solve(input, n=1, m=1):
    input = input[:]
    l = len(input)
    if m != 1: input = [(i, v*m) for i, v in input]
    for x in range(n):
        print(x, end="\r")
        for e in range(len(input)):
            for ti, (i, v) in enumerate(input):
                if i == e:
                    if v == 0: break
                    ni = (ti + v) % (l-1)
                    input.pop(ti)
                    input = input[:ni] + [(i, v)] + input[ni:]
                    break
    input = [v for i, v in input]
    iz = input.index(0)
    return input[(iz+1000)%l] + input[(iz+2000)%l] + input[(iz+3000)%l]

input = open("20_input").readlines()
input = [(i, int(v)) for i, v in enumerate(input)]

print(f"Part one: {solve(input)}")
print(f"Part two: {solve(input, n=10, m=811589153)}")