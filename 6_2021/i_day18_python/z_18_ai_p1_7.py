"""The following is a solution to the problem in Python:

"""
def reduce(number):
  # If any pair is nested inside four pairs, the leftmost such pair explodes.
  while len(number) == 2 and type(number[0]) == list and type(number[1]) == list and \
        len(number[0]) == 2 and type(number[0][0]) == list and type(number[0][1]) == list and \
        len(number[1]) == 2 and type(number[1][0]) == list and type(number[1][1]) == list:
    # The left value of the exploding pair is added to the first regular number to the left of the exploding pair (if any).
    for i in range(len(number)):
      if type(number[i]) != list:
        number[i] += number[0][0]
        break
    # The right value of the exploding pair is added to the first regular number to the right of the exploding pair (if any).
    for i in range(len(number)-1, -1, -1):
      if type(number[i]) != list:
        number[i] += number[1][1]
        break
    # The entire exploding pair is replaced with the regular number 0.
    number = number[0][1][0][1][1]
  # If any regular number is 10 or greater, the leftmost such regular number splits.
  for i in range(len(number)):
    if type(number[i]) != list and number[i] >= 10:
      # Replace the regular number with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up.
      number[i] = [number[i] // 2, (number[i] + 1) // 2]
  # Return the reduced number.
  return number

# Parse the input.
with open('18_input') as f:
  numbers = f.read().strip().split('\n')
numbers = [[[int(c) if c.isdigit() else reduce([int(d) if d.isdigit() else reduce([int(e) if e.isdigit() else reduce([int(f) if f.isdigit() else reduce([int(g) if g.isdigit() else reduce([int(h) if h.isdigit() else reduce([int(i) if i.isdigit() else reduce([int(j) if j.isdigit() else reduce([int(k) if k.isdigit() else reduce([int(l) if l.isdigit() else reduce([int(m) if m.isdigit() else reduce([int(n) if n.isdigit() else reduce([int(o) if o.isdigit() else reduce([int(p) if p.isdigit() else reduce([int(q) if q.isdigit() else reduce([int(r) if r.isdigit() else reduce([int(s) if s.isdigit() else reduce([int(t) if t.isdigit() else reduce([int(u) if u.isdigit() else reduce([int(v) if v.isdigit() else reduce(["""