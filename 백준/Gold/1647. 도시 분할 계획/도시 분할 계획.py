import sys

sys.setrecursionlimit(10 ** 5)
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
edges = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

uf = [i for i in range(n + 1)]

ans = []

for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        ans.append(w)

print(sum(ans) - max(ans))
