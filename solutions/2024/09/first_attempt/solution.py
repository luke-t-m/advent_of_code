#!/usr/bin/python3
import sys

p1 = p2 = 0
inp = sys.argv[1].strip()

disk = []

id = 0
is_file = True
for i in inp:
    if is_file:
        to_app = id
        id += 1
    else:
        to_app = -1
    is_file = not is_file
    for j in range(int(i)):
        disk.append(to_app)
    
at = 0
while at < len(disk):
    if disk[at] == -1:
        while (i := disk.pop()) == -1:
            pass
        disk[at] = i
    at += 1

for i, v in enumerate(disk):
    p1 += i * v

# part 2.
disk = []
id = 0
is_file = True
for i in inp:
    if is_file:
        to_app = id
        id += 1
    else:
        to_app = -1
    is_file = not is_file
    size = int(i)
    disk.append((to_app, size))

disk2 = disk[::-1]


for (id, size) in disk2:
    if id == -1:
        continue
    for i, (id2, size2) in enumerate(disk):
        if id2 == id:
            break
        if id2 == -1 and size <= size2:
            disk[i] = (id, size)
            diff = size2 - size
            if diff != 0:
                disk.insert(i+1, (-1, diff))
            break

disk2 = []

seen = set()
for (id, size) in disk:
    if id not in seen:
        to_add = id
        seen.add(id)
    else:
        to_add = -1
    disk2 += size * [to_add]

for i, v in enumerate(disk2):
    if v != -1:
        p2 += i * v


print(p1, p2)