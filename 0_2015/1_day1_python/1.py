input = open("input").read()

print(input.count("(") - input.count(")"))

f = 0
for c, v in enumerate(input):
    if v == "(": f += 1
    elif v == ")": f -= 1
    if f == -1:
        print(c + 1)
        break
