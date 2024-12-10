import sys

sys.setrecursionlimit(10 ** 6)


def union(a, b):
    x, y = find(a), find(b)
    uf[x] = y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m = map(int, input().split())
uf = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, input().split())
    if not command:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')
