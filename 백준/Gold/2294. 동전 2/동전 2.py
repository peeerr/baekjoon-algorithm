import sys

n, k = map(int, sys.stdin.readline().split())
coin_types = [ int(sys.stdin.readline()) for _ in range(n) ]

d = [10001] * (k + 1)
d[0] = 0

for i in coin_types:
    for j in range(i, k + 1):
        if d[j - i] != 10001:
            d[j] = min(d[j], d[j - i] + 1)

print(-1) if d[k] == 10001 else print(d[k])
