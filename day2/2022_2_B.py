from aocd import lines

points = {'X': 1, 'Y': 2, 'Z': 3}
convert = {'A': 'X', 'B': 'Y', 'C': 'Z'}
arr = ['X', 'Y', 'Z']

get_item = lambda item, i: arr[(arr.index(item) + i) % len(arr)]
score = 0

for line in lines:
    op, verdict = convert[line[0]], line[2]
    if verdict == 'X':
        score += points[get_item(op, -1)]
    elif verdict == 'Y':
        score += 3 + points[op]
    else:
        score += 6 + points[get_item(op, 1)]
print(score)
