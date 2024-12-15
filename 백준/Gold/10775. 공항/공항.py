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


g = int(input())
p = int(input())
gates = [int(input()) for _ in range(p)]

ans = 0
uf = [i for i in range(g + 1)]

for gate in gates:
    parent = find(gate)
    if not parent:
        break
    ans += 1
    union(parent, parent - 1)

print(ans)
