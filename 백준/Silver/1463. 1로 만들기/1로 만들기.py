import sys

n = int(sys.stdin.readline())
d = [0] * (n + 1)

for x in range(2, n + 1):
    d[x] = d[x - 1] + 1

    if x % 3 == 0:
        d[x] = min(d[x // 3] + 1, d[x])
    if x % 2 == 0:
        d[x] = min(d[x // 2] + 1, d[x])

print(d[-1])
