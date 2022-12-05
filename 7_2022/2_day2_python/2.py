lines = open("input").readlines()

def asc(char): return int.from_bytes(char.encode(), "big")
        
print(f"Part one: {sum(map(lambda l: ((asc(l[2])-asc(l[0])-23)%3+1)%3*3+asc(l[2])-87, lines))}")
print(f"Part two: {sum(map(lambda l: ((3*(asc(l[2])-89)+asc(l[0])-64)+3+2*(87-asc(l[2])))%3+1+3*(asc(l[2])-88), lines))}")