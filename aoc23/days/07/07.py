card_scores = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "J2": 1}
card_scores.update(({str(x): x for x in range(9, 1, -1)}))


def get_counts(hand):
    seen = dict()
    for card in hand:
        if card == "J2":
            continue
        if card not in seen:
            seen[card] = 0
        seen[card] += 1
    return sorted(seen.values(), reverse=True) + [0, 0]


def score(hand, is_p2=False):
    if is_p2:
        hand = ["J2" if i == "J" else i for i in hand]
    counts = get_counts(hand)
    c1 = counts[0]
    if is_p2:
        c1 += hand.count("J2")
    c2 = counts[1]
    if c1 >= 5:
        out = "6"
    elif c1 == 4:
        out = "5"
    elif c1 == 3 and c2 >= 2:
        out = "4"
    elif c1 == 3:
        out = "3"
    elif c1 == 2 and c2 == 2:
        out = "2"
    elif c1 == 2:
        out = "1"
    else:
        out = "0"
    out += "".join([str(card_scores[card]).zfill(2) for card in hand])
    return int(out)


def solve(hands, key):
    hands.sort(key=key)
    return sum(bid * ind for (ind, (_, bid)) in enumerate(hands, 1))


with open("input") as file:
    raw = file.read()

hands = raw.strip().split("\n")
hands = [(list((parts := hand.split(" "))[0]), int(parts[1])) for hand in hands]

score_p1 = lambda x: score(x[0])
score_p2 = lambda x: score(x[0], is_p2=True)

p1 = solve(hands, score_p1)
p2 = solve(hands, score_p2)
print(p1, p2)
