ls = open("input").readlines()

alpha = "abcdefghijklmnopqrstuvwxyz"
total_id = 0
for l in ls:
    l = l.split("-")
    t = ""
    for s in l:
        if s[0] in "0123456789":
            sec_id = int(s[:-8])
            f_lets = list(s[-7:-2])
        else:
            t += s
    decoded = "".join([alpha[(alpha.find(s) + sec_id) % 26] for s in t]) # then just use grep on output lol
    if "north" in decoded: print(f"Task 2: {decoded} {sec_id}")
    counts = sorted(sorted("".join(set(t))), key=t.count, reverse = True)[:5]
    if sorted(counts) == sorted(list(f_lets)): total_id += sec_id

print(f"Task 1: {total_id}")
