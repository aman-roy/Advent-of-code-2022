from aocd import numbers

points = 0
for num in numbers:
    num = list(map(lambda x: abs(x), num))
    points += 1 if len(set(range(num[0], num[1] + 1)).intersection(range(num[2], num[3] + 1))) else 0
print(points)
