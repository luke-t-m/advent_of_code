with open("input") as file:
    raw = file.read()

lines = raw.strip().split("\n")
p1 = p2 = 0

for line in lines:
    diffs = [[int(x) for x in line.split()]]
    while not all(i == 0 for i in diffs[-1]):
        cur = diffs[-1]
        diffs.append([j - i for i, j in zip(cur[:-1], cur[1:])])

    p1 += sum([x[-1] for x in diffs])
    wrk = 0
    for diff in diffs[::-1]:
        wrk = diff[0] - wrk
    p2 += wrk

print(p1, p2)
