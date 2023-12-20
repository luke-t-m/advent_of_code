from collections import deque
from functools import reduce



with open("20/input") as file:
    raw = file.read()

lines = raw.strip().split("\n")

modules = dict()
for line in lines:
    name, dests = line.split(" -> ")
    dests = dests.split(", ")
    if name == "broadcaster":
        broadcast = dests
    else:
        type = name[0]
        name = name[1:]
        if type == "%":
            modules[name] = (type, dests, [0])
        elif type == "&":
            modules[name] = (type, dests, dict())

for name, (type, dests, wrk) in modules.items():
    for dest in dests:
        if dest in modules and modules[dest][0] == "&":
            modules[dest][2][name] = 0

pulses = deque([("broadcaster", dest, 0) for dest in broadcast])

sent = [0, 0]

cycles = dict()

for press in range(100000):
    pulses = deque([("broadcaster", dest, 0) for dest in broadcast])
    sent[0] += len(broadcast) + 1
    while len(pulses) != 0:
        source, at, hilo = pulses.popleft()
        type, dests, wrk = modules[at]
        to_send = None
        if type == "%":
            if hilo == 0:
                wrk[0] = 1 - wrk[0]
                to_send = wrk[0]
        elif type == "&":
            wrk[source] = hilo
            to_send = 1 - int(all(i == 1 for i in wrk.values()))

        if to_send is not None:
            sent[to_send] += len(dests)
            for dest in dests:
                if dest != "rx":
                    pulses.append((at, dest, to_send))

                wrk = modules["ls"][2]
                for i in wrk:
                    if wrk[i] == 1:
                        cycles[i] = press + 1
                if len(cycles) == 4:
                    print(reduce(lambda a, b: a * b, cycles.values(), 1))
                    exit()
    if press == 1000:
        print(sent[0] * sent[1])






