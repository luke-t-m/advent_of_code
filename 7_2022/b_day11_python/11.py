#!/usr/bin/env python3
import gmpy2
input = open("11_input").readlines()
#input = open("11_test").readlines()

monkeys =[{"items": [84, 72, 58, 51], "op": lambda x: x * 3, "test": lambda x: x % 13 == 0, "if_true": 1, "if_false": 7, "no_inspects": 0, "div":13},
          {"items": [88, 58, 58], "op": lambda x: x + 8, "test": lambda x: x % 2 == 0, "if_true": 7, "if_false": 5, "no_inspects": 0, "div":2},
          {"items": [93, 82, 71, 77, 83, 53, 71, 89], "op": lambda x: x * x, "test": lambda x: x % 7 == 0, "if_true": 3, "if_false": 4, "no_inspects": 0, "div":7},
          {"items": [81, 68, 65, 81, 73, 77, 96], "op": lambda x: x + 2, "test": lambda x: x % 17 == 0, "if_true": 4, "if_false": 6, "no_inspects": 0, "div":17},
          {"items": [75, 80, 50, 73, 88], "op": lambda x: x + 3, "test": lambda x: x % 5 == 0, "if_true": 6, "if_false": 0, "no_inspects": 0, "div":5},
          {"items": [59, 72, 99, 87, 91, 81], "op": lambda x: x * 17, "test": lambda x: x % 11 == 0, "if_true": 2, "if_false": 3, "no_inspects": 0, "div":11},
          {"items": [86, 69], "op": lambda x: x + 6, "test": lambda x: x % 3 == 0, "if_true": 1, "if_false": 0, "no_inspects": 0, "div":3},
          {"items": [91], "op": lambda x: x + 1, "test": lambda x: x % 19 == 0, "if_true": 2, "if_false": 5, "no_inspects": 0, "div":19}
]
"""
monkeys =[{"items": [79, 98], "op": lambda x: x * 19, "test": lambda x: x % 23 == 0, "if_true": 2, "if_false": 3, "no_inspects": 0, "div":23},
          {"items": [54, 65, 75, 74], "op": lambda x: x + 6, "test": lambda x: x % 19 == 0, "if_true": 2, "if_false": 0, "no_inspects": 0, "div":19},
          {"items": [79, 60, 97], "op": lambda x: x*x, "test": lambda x: x % 13 == 0, "if_true": 1, "if_false": 3, "no_inspects": 0, "div":13},
          {"items": [74], "op": lambda x: x + 3, "test": lambda x: x % 17 == 0, "if_true": 0, "if_false": 1, "no_inspects": 0, "div":17}
]
"""
for round in range(20):
  for m in monkeys:
    #m["items"] = list(map(lambda x: m["op"](x) // 3, m["items"]))
    #m["no_inspects"] += len(m["items"])
    for i in m["items"]:
      m["no_inspects"] += 1
      j = m["op"](i) // 3
      if m["test"](j):
        monkeys[m["if_true"]]["items"].append(j)
      else:
        monkeys[m["if_false"]]["items"].append(j)
    m["items"] = []

nos = []
for x in monkeys: nos.append(x["no_inspects"])
nos.sort(reverse=True)
print(f"Part one: {nos[0] * nos[1]}")


# p2
for m in monkeys:
  map(gmpy2.mpz, m["items"])
  m["mod"] = []
  m["no_inspects"] = 0
  for i in m["items"]:
    m["mod"].append([0] + [i % v for v in range(1, 24)])

for round in range(10000):
  for m in monkeys:
    #m["items"] = list(map(lambda x: m["op"](x) // 3, m["items"]))
    #m["no_inspects"] += len(m["items"])
    for i in m["mod"]:
      m["no_inspects"] += 1
      j = list(map(m["op"], i))
      if m["test"](j[m["div"]]):
        monkeys[m["if_true"]]["mod"].append([0] + [j[v] % v for v in range(1, 24)])
      else:
        monkeys[m["if_false"]]["mod"].append([0] + [j[v] % v for v in range(1, 24)])
    m["mod"] = []
  #if round % 100 == 0: print(round)

nos = []
for x in monkeys:
  nos.append(x["no_inspects"])
nos.sort(reverse=True)
print(f"Part two: {nos[0] * nos[1]}")
