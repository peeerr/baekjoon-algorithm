import sys

input = sys.stdin.readline

T = int(input())
arr = [int(input()) for _ in range(T)]

d = [0] * 11
d[0] = 1
d[1] = 2
d[2] = 4

for n in arr:
    for i in range(3, n):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    print(d[n - 1])
