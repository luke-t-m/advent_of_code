#!/usr/bin/env python3

input = open("6_input").read()

def unique_last(d, n):
    for i in range(n, len(d)):
        last = d[i-(n-1): i+1]
        if sorted(list(last)) == sorted(set(last)): return i+1

print(f"Part one: {unique_last(input, 4)}")
print(f"Part one: {unique_last(input, 13)}")
