import hashlib
 

def solve(input, do_pos = False):
    out = [""] * 8
    num = 0
    while len([x for x in out if x != ""]) < 8:
        hash = hashlib.md5((input + str(num)).encode('utf-8')).hexdigest()
        if hash[:5] == "00000":
            try:
                if do_pos: pos, val = int(hash[5]), hash[6]
                else: pos, val = out.index(""), hash[5]
                if out[pos] == "": out[pos] = val
            except:
                print("fail")
        num += 1
        if num % 100000 == 0: print(f"{hash} {out}") # hacking "animation"
    return "".join(out)


input = "reyedfim"

task_one = solve(input)
task_two = solve(input, do_pos = True)

print(f"Part one: {task_one}\nPart two: {task_two}")
