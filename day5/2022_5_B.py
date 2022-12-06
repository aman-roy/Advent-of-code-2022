from aocd import lines
import re

# every stack from bottom to up
stack = ["HTZD", "QRWTGCS", "PBFQNRCH", "LCNFHZ", "GLFQS", "VPWZBRCS", "ZFJ", "DLVZRHQ", "BHGNFZLD"]

for line in lines[10:]:
    num = [int(x) for x in re.findall(r'\d+', line)]
    stack[num[2] - 1] += stack[num[1] - 1][-num[0]:]
    stack[num[1] - 1] = stack[num[1] - 1][:len(stack[num[1] - 1]) - num[0]]

print(''.join(list(map(lambda x: x[-1], stack))))
