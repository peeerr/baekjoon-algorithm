import sys

n = int(sys.stdin.readline())
d = [0] * n

if n == 1 or n == 2:
    print(1)
else:
    d[0] = 1
    d[1] = 1

    for i in range(2, n):
        d[i] = d[i - 1] + d[i - 2]

    print(d[n - 1])
