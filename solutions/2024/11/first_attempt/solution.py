#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
from collections import defaultdict

def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)

p1 = p2 = 0
inp = sys.argv[1]


for _ in range(25):
    break
    to_add = []
    for i, stone in enumerate(stones):
        stone_str = f"{stone}"
        len_stone_str = len(stone_str)
        if stone == 0:
            stones[i] = 1
        elif len_stone_str % 2 == 0:
            half = len_stone_str // 2
            fst = int(stone_str[:half])
            snd = int(stone_str[half:])
            stones[i] = fst
            to_add.append((i, snd))
        else:
            stones[i] = stone * 2024
    for mod, add in enumerate(to_add):
        i, v = add
        stones.insert(i + mod, v)


def solve(n):
    stones = defaultdict(lambda: 0)
    for num in map(int, inp.split()):
        stones[num] += 1

    for _ in range(n):
        to_add = defaultdict(lambda: 0)
        for num in stones:
            num_str = f"{num}"
            len_num = len(num_str)
            no_num = stones[num]
            to_add[num] -= no_num
            if num == 0:
                to_add[1] += no_num
            elif len_num % 2 == 0:
                half = len_num // 2
                fst = int(num_str[:half])
                snd = int(num_str[half:])
                to_add[fst] += no_num
                to_add[snd] += no_num
            else:
                to_add[num * 2024] += no_num
        for num in to_add:
            stones[num] += to_add[num]

    out = 0
    for num in stones:
        out += stones[num]
    return out

p1 = solve(25)
p2 = solve(75)

output(p1)
output(p2)