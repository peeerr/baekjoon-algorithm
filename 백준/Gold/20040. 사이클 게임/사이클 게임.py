import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m = map(int, input().split())
uf = [i for i in range(n + 1)]

ans = 0

for cnt in range(1, m + 1):
    x, y = map(int, input().split())
    if find(x) == find(y):
        ans = cnt
        break
    else:
        union(x, y)

print(ans)
