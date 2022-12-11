#!/usr/bin/env python3
import re

class Monkey:
  no_inspects = 0

  def __init__(self, is_p2, items, mods, op, div, if_t, if_f):
    if is_p2: self.items = [dict((m, v % m) for m in mods) for v in items]
    else: self.items = items
    self.op = op
    self.div = int(div)
    self.if_t = int(if_t)
    self.if_f = int(if_f)

  def __str__(self):
    return f"A willing participant in the random chimp event of 2022. Items: {self.items} div: {self.div}"

  def update_inspects(self):
    self.no_inspects += len(self.items)


def parse_op(string):
  m = re.search("Operation: new = old (.*) (.*)", string)
  if m.group(2) == "old": return lambda x: x ** 2
  if m.group(1) == "*": return lambda x: x * int(m.group(2))
  if m.group(1) == "+": return lambda x: x + int(m.group(2))

def rounds_p1(monkeys, rounds):
  for n in range(rounds):
    for m in monkeys:
      m.update_inspects()
      for i in m.items:
        j = m.op(i) // 3
        if j % m.div == 0: monkeys[m.if_t].items.append(j)
        else: monkeys[m.if_f].items.append(j)
      m.items = []

def rounds_p2(monkeys, rounds):
  for n in range(rounds):
    for m in monkeys:
      m.update_inspects()
      for i in m.items:
        j = {k: m.op(v) for k, v in i.items()}
        jm = {k: v % k for k, v in j.items()}
        if j[m.div] % m.div == 0: monkeys[m.if_t].items.append(jm)
        else: monkeys[m.if_f].items.append(jm)
      m.items = []

def best_monkeys(monkeys):
  monkeys = sorted(map(lambda x: x.no_inspects, monkeys), reverse = True)
  return monkeys[0] * monkeys[1]

def solve(input, is_p2, rounds):
  monkeys = []
  mods = [*map(int, re.findall("Test: divisible by (\d+)", input))]
  input = input.split("\n\n")
  for monke in input:
    monke = monke.split("\n")
    items = [*map(int, re.findall("\d+", monke[1]))]
    op = parse_op(monke[2])
    div = re.search("Test: divisible by (\d+)", monke[3]).group(1)
    if_t = re.search("If true: throw to monkey (\d+)", monke[4]).group(1)
    if_f = re.search("If false: throw to monkey (\d+)", monke[5]).group(1)

    monkeys.append(Monkey(is_p2, items, mods, op, div, if_t, if_f))

  if is_p2: rounds_p2(monkeys, rounds)
  else: rounds_p1(monkeys, rounds)
  return best_monkeys(monkeys)

input = open("11_input").read().strip()

print(f"Part one: {solve(input, False, 20)}")
print(f"Part two: {solve(input, True, 10000)}")
