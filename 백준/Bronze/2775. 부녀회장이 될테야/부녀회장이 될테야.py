import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    d = [[0 for _ in range(n)] for _ in range(k + 1)]
    d[0] = [i for i in range(1, n + 1)]

    for i in range(1, k + 1):
        for j in range(n):
            d[i][j] = sum(d[i - 1][:j+1])

    print(d[-1][-1])
