from aocd import numbers

points = 0
for num in numbers:
    num = list(map(lambda x: abs(x), num))
    points += 1 if (num[0] <= num[2] and num[1] >= num[3]) or (num[2] <= num[0] and num[3] >= num[1]) else 0
print(points)
