from aocd import lines
from string import ascii_letters

print(sum(ascii_letters.index(''.join(set(line[:len(line) // 2]).intersection(line[len(line) // 2:]))) + 1 for line in lines))
