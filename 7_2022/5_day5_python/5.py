#!/usr/bin/env python3

input = open("5_input").readlines()
#input = open("5_test").readlines()

def find_first_sublist(seq, sublist, start=0):
    for i in range(start, len(seq)):
        if seq[i:i + len(sublist)] == sublist: return i, i + len(sublist)

def replace_sublist(seq, sublist, replacement, i = 0):
    for start, end in iter(lambda: find_first_sublist(seq, sublist, i), None):
        seq[start:end], i = replacement, start + len(replacement)

def deepEnoughCopy(L):
    return [L[i][:] for i in range(len(L))]

reading_instr = False
instr, state, columns = [], [], []
for line in input:
    line = line[:-1]
    if line == "": continue
    if " 1   2   3" in line:
        reading_instr = True
        continue

    line = line.split(" ")
    if reading_instr:
        instr.append(list(map(int, (line[1], line[3], line[5]))))
    else:
        replace_sublist(line, ["", "", "", ""], [""])
        state.append(line)

for i in state[0]: columns.append([])

for i in state:
    for c, v in enumerate(i):
        if v != "": columns[c].append(v[1])

def solve(columns, do_part_two = False):
    for i in instr:
        buffer = []
        for j in range(i[0]):
            try:
                if do_part_two: buffer += [columns[i[1]-1].pop(0)]
                else: columns[i[2]-1] = [columns[i[1]-1].pop(0)] + columns[i[2]-1]
            except: pass
        if do_part_two: columns[i[2]-1] = buffer + columns[i[2]-1]

    return "".join([i[0] for i in columns if i != []])

cols1 = deepEnoughCopy(columns)
cols2 = deepEnoughCopy(columns)
print(f"Part one: {solve(cols1)}")
print(f"Part two: {solve(cols2, True)}")


