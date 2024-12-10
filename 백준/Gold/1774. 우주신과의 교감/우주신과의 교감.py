import sys

input = sys.stdin.readline


def calc_dist(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m = map(int, input().split())
pos = [0] + [tuple(map(int, input().split())) for _ in range(n)]
edges = []

for i in range(1, n + 1):
    x1, y1 = pos[i]
    for j in range(i + 1, n + 1):
        x2, y2 = pos[j]
        dist = calc_dist(x1, y1, x2, y2)
        edges.append((i, j, dist))

edges.sort(key=lambda x: x[2])
uf = [i for i in range(n + 1)]

channels = [tuple(map(int, input().split())) for _ in range(m)]

for i, j in channels:
    union(i, j)

ans = 0

for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        ans += w

print(f"{ans:.2f}")
