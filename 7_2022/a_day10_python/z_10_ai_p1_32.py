"""The following code solves the problem described above.

"""
def solve():
    x = 1
    strength = 0
    with open("10_input") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if line == "noop":
                pass
            else:
                v = int(line.split()[1])
                x += v
                if i == 19 or (i - 19) % 40 == 0:
                    strength += i * x
    print(strength)

solve()
""""""