lines = open("input").readlines()
#lines = open("test").readlines()


# plays in format: play, wins against, draws with, loses to
plays = {"A" : ("Z", "X", "Y"),
         "B" : ("X", "Y", "Z"),
         "C" : ("Y", "Z", "X")}

moves = plays["B"]

def solve(lines, part_two = False, score = 0):
    for line in lines:
        opp, you = line[0], line[2]
        if part_two: score += moves.index(plays[opp][moves.index(you)] ) + 1 + moves.index(you) * 3
        else: score += moves.index(you) + 1 + plays[opp].index(you) * 3
    return score

print(f"Part one: {solve(lines)}")
print(f"Part two: {solve(lines, True)}")