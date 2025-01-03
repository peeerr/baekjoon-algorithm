import sys

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

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

ans = set()
for x in range(1, n + 1):
    ans.add(find(x))

print(len(ans))
