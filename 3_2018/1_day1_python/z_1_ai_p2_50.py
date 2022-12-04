"""The following code reads from a file called "1_input" and prints the first frequency that is reached twice:

"""
frequencies = []

with open("1_input") as file:
  for line in file:
    frequencies.append(int(line))

current_frequency = 0
reached_frequencies = set([current_frequency])

while True:
  for frequency in frequencies:
    current_frequency += frequency
    if current_frequency in reached_frequencies:
      print(current_frequency)
      exit()
    reached_frequencies.add(current_frequency)
""""""