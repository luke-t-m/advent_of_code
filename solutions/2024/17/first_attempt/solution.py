#!/usr/bin/python3
import sys
from subprocess import run as subprocess_run
import regex as re
from collections import deque
def output(val):
    if val != 0:
        subprocess_run(["xsel", "--clipboard"], input=f"{val}".encode())
    print(val)

def startsWithSublist(l,sub):
    return len(sub) <= len(l) and all(l[i] == el  for i,el  in enumerate(sub))



class Computer():
    def __init__(self, reg, program):
        self.opcodes = {0: self.adv,
                        1: self.bxl,
                        2: self.bst,
                        3: self.jnz,
                        4: self.bxc,
                        5: self.out,
                        6: self.bdv,
                        7: self.cdv}
        self.og_reg = reg
        self.program = program
        self.reset()

    def reset(self):
        self.reg = self.og_reg
        self.ptr = 0
        self.result = []

    def set_reg_a(self, reg_a):
        self.reg[0] = reg_a

    def combo(self, i):
        if i <= 3:
            return i
        if i == 4:
            return self.reg[0]
        if i == 5:
            return self.reg[1]
        if i == 6:
            return self.reg[2]

    def literal(self, i):
        return i

    def dv(self, i):
        return self.reg[0] // (2 ** self.combo(i))

    def adv(self, i):
        self.reg[0] = self.dv(i)

    def bxl(self, i):
        self.reg[1] = self.reg[1] ^ self.literal(i)

    def bst(self, i):
        self.reg[1] = self.combo(i) % 8

    def jnz(self, i):
        if self.reg[0] != 0:
            self.ptr = self.literal(i) - 2

    def bxc(self, _):
        self.reg[1] = self.reg[1] ^ self.reg[2]

    def out(self, i):
        self.result.append(self.combo(i) % 8)

    def bdv(self, i):
        self.reg[1] = self.dv(i)

    def cdv(self, i):
        self.reg[2] = self.dv(i)

    def run_program(self):
        while self.ptr < len(self.program):
            instr = self.program[self.ptr]
            oper = self.program[self.ptr + 1]
            self.opcodes[instr](oper)
            self.ptr += 2

    def run_program_shortcircuit(self, want):
        while self.ptr < len(program):
            instr = self.program[self.ptr]
            oper = self.program[self.ptr + 1]
            self.opcodes[instr](oper)
            self.ptr += 2
            if not startsWithSublist(want, self.result):
                return

    def get_result(self):
        return self.result
    
    def pretty_result(self, delimiter=""):
        return delimiter.join(str(i) for i in self.result)
    

p1 = p2 = 0
inp = sys.argv[1]

re_string = "Register A: (\d*)\nRegister B: (\d*)\nRegister C: (\d*)\n\nProgram: ([\d,\,]*)"
matched = re.match(re_string, inp)
og_reg = [int(i) for i in matched.groups()[:3]]
program_str = matched.groups()[3].split(",")
program = [int(i) for i in program_str]
want = "".join(program_str[::-1])

comp = Computer(og_reg, program)
comp.run_program()
p1 = comp.pretty_result(",")

dq = deque([(0, 2**45, 2**48-1)])

best = 10**100
while dq:
    at, lower, upper = dq.popleft()
    if at >= len(want):
        continue
    middle = (lower + upper) // 2
    if middle == lower or middle == upper:
        continue
    nat = at + 1
    comp.reset()
    comp.set_reg_a(lower)
    comp.run_program()
    lower_out = comp.pretty_result()[::-1]
    comp.reset()
    comp.set_reg_a(upper)
    comp.run_program()
    upper_out = comp.pretty_result()[::-1]
    if upper_out == want:
        best = min(best, upper)
    if lower_out == want:
        best = min(best, lower)
    if upper_out[:nat] == lower_out[:nat]:
        if upper_out[:nat] == want[:nat]:
            dq.appendleft((nat, lower, middle))
            dq.appendleft((nat, middle, upper))
    else:
        dq.append((at, lower, middle))
        dq.append((at, middle, upper))

for reg_a in range(best, best-2**10, -1):
    comp.reset()
    comp.set_reg_a(reg_a)
    comp.run_program()
    out = comp.pretty_result()[::-1]
    if out == want:
        p2 = reg_a

output(p1)
output(p2)