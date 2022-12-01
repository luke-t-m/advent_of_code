lines = open("input").readlines()


calories = [0]
for line in lines:
    if line == "\n": calories.append(0)
    else: calories[-1] += int(line)

calories.sort()
print(f"Part 1: {calories[-1]}")
print(f"Part 2: {sum(calories[:-4:-1])}")
