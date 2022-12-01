lines = open("input").readlines()


calories = [0]
for line in lines:
    if line == "\n": calories.append(0)
    else: calories[-1] += int(line)

print(f"Part 1: {max(calories)}")
print(f"Part 2: {sum(sorted(calories, reverse = True)[:3])}")
