from aocd import lines
from string import ascii_letters

print(sum(ascii_letters.index(''.join(set(sublist[2]).intersection(''.join(set(sublist[0]).intersection(sublist[1])))))+1 for sublist in [lines[i:i+3] for i in range(0, len(lines), 3)]))


