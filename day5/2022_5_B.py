#         [H]         [S]         [D]
#     [S] [C]         [C]     [Q] [L]
#     [C] [R] [Z]     [R]     [H] [Z]
#     [G] [N] [H] [S] [B]     [R] [F]
# [D] [T] [Q] [F] [Q] [Z]     [Z] [N]
# [Z] [W] [F] [N] [F] [W] [J] [V] [G]
# [T] [R] [B] [C] [L] [P] [F] [L] [H]
# [H] [Q] [P] [L] [G] [V] [Z] [D] [B]
#  1   2   3   4   5   6   7   8   9

from aocd import lines
import re

# every stack from bottom to up
stack = ["HTZD", "QRWTGCS", "PBFQNRCH", "LCNFHZ", "GLFQS", "VPWZBRCS", "ZFJ", "DLVZRHQ", "BHGNFZLD"]

for line in lines[10:]:
    num = [int(x) for x in re.findall(r'\d+', line)]
    stack[num[2] - 1] += stack[num[1] - 1][-num[0]:]
    stack[num[1] - 1] = stack[num[1] - 1][:len(stack[num[1] - 1]) - num[0]]

print(''.join(list(map(lambda x: x[-1], stack))))
