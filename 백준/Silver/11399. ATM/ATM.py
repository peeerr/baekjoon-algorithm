import sys

input = sys.stdin.readline

n = int(input())
p = sorted(map(int, input().split()))

d = [0] * n
d[0] = p[0]

for i in range(1, len(p)):
    d[i] = d[i - 1] + p[i]

print(sum(d))
