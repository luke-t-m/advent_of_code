file = open("input")
raw = file.readlines()
file.close()

subs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for line in raw:
  for num, word in enumerate(subs):
      line = line.replace(word, word[0] + str(num+1) + word[-1])
  line = ''.join(c for c in line if c.isdigit())
  sum += int(line[0] + line[-1])


print(sum)