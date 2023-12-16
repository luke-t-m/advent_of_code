with open("input") as file:
    raw = file.read()


def hash(string):
    out = 0
    for c in string:
        out += ord(c)
        out *= 17
        out %= 256
    return out


parts = raw.strip().split(",")

p1 = sum(hash(i) for i in parts)

boxes = [dict() for _ in range(256)]

for part in parts:
    if part[-1] == "-":
        label = part[:-1]
        label_hash = hash(label)
        if label in boxes[label_hash]:
            del boxes[label_hash][label]
    elif part[-2] == "=":
        label, lens = part.split("=")
        boxes[hash(label)][label] = int(lens)


p2 = sum(
    (1 + i) * (1 + i2) * lens
    for i, box in enumerate(boxes)
    for i2, (_, lens) in enumerate(box.items())
)

print(p1, p2)
