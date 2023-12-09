
with open("input") as file:
    raw = file.read()
cards = raw.strip().split("\n")

p1 = 0
wins = []


def score(card):
    card = card.split(":")[1]
    want, have = card.split("|")
    want = want.split()
    have = have.split()
    score = 0
    for num in have:
        if num in want:
            score += 1
    return score


for i, card in enumerate(cards):
    s = score(card)
    p1 += int(2 ** (s - 1))
    wins.append([])
    for j in range(i + 1, i + s + 1):
        wins[-1].append(j)


nos = [1] * len(cards)

for at in range(len(cards)):
    for dupe in wins[at]:
        nos[dupe] += nos[at]

print(p1, sum(nos))
