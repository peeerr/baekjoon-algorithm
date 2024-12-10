import sys 

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m, t = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

uf = [i for i in range(n + 1)]
ans = sum([t * i for i in range(n - 1)])

for v, u, w in edges:
    if find(v) != find(u):
        ans += w
        union(v, u)

print(ans)
