input = open("input").readlines()

print(f"Part one: {sum(map(lambda l: (((ord((set(l[:len(l)//2])&set(l[len(l)//2:])).pop())-65))%65+27)%58, input))}")
print(f"Part two: {sum(map(lambda l: ((((ord(((set(l[0])&set(l[1])&set(l[2]))).difference(chr(10)).pop()))-65))%65+27)%58, zip(input[::3], input[1::3], input[2::3])))}")
