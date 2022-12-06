from aocd import get_data
import re

print(sorted([sum(map(lambda x: int(x), list(re.findall('\d+', x)))) for x in get_data(day=1, year=2022).split('\n\n')], reverse=True)[0])
