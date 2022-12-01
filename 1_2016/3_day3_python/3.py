
def solve(lines):
    return len([a for a in lines if a[0] + a[1] > a[2] and a[0] + a[2] > a[1] and a[1] + a[2] > a[0]])

lines = open("input").readlines()

lines = list(map(lambda x: [int(y) for y in x.split(" ") if y != ""], lines))

print(f"Part 1: {solve(lines)}")

new_lines = []
for c in lines:
    l = len(new_lines)
    if l == len([x for x in new_lines if len(x) == 3]):
        new_lines += [[c[0]], [c[1]], [c[2]]]
    else:
        for i in range(3): new_lines[l - (3-i)].append(c[i])

print(f"Part 2: {solve(new_lines)}")
