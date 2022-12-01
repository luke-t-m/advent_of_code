input = open("input").readlines()

sum = 0
rib = 0
for line in input:
    [l, w, h] = map(int, line.split("x"))
    sum += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    rib += min(2*l + 2*w, 2*w + 2*h, 2*h + 2*l) + l * w * h

print(f"Part one: {sum}\nPart two: {rib}")