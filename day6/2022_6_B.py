from aocd import get_data

x = 14
data = get_data().strip()
print([(i + x) for i in range(len(data)) if len(set(data[i: i+x])) == x][0])
