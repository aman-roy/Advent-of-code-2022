from aocd import lines

points = {'X': 1, 'Y': 2, 'Z': 3}
convert = {'A': 'X', 'B': 'Y', 'C': 'Z'}
arr = ['X', 'Y', 'Z']

get_item = lambda item, i: arr[(arr.index(item) + i) % len(arr)]
score = 0

for line in lines:
    op, me = convert[line[0]], line[2]
    score += points[me]
    if get_item(op, 1) == me:
        score += 6
    elif get_item(op, 0) == me:
        score += 3
print(score)
