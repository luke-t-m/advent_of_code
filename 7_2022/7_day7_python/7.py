#!/usr/bin/env python3

input = open("7_input").readlines()

lines = list(map(lambda x: x.strip(), input))

path = ""
sizes = dict()
ls_mode = False
for i in lines:
  h = i.split(" ")
  u = h[0]
  s = h[1]
  if len(h) == 3: t = h[2]
  if s == "ls":
    ls_mode = True
    continue
  if ls_mode:
    if u == "$": ls_mode = False
    elif u != "dir":
      tmp_path = path
      while tmp_path != "":
        try: sizes[tmp_path] += int(u)
        except: sizes[tmp_path] = int(u)
        tmp_path = "/".join(tmp_path.split("/")[:-1])
  if s == "cd":
    if t == "/": path = "/"
    elif t == "..": path = "/".join(path.split("/")[:-1])
    else: path += "/" + t


print(f"Part one: {sum([sizes[dir] for dir in sizes if sizes[dir] < 100000])}")

total = 70000000
need = total - 30000000
print(f"Part two: {min([sizes[dir] for dir in sizes if sizes['/'] - sizes[dir] <= need])}")
