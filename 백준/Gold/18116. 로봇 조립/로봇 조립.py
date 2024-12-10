import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INT_MAX = 1000000


def union(x, y):
    X, Y = find(x), find(y)
    if X != Y:
        uf[X] = Y
        size[Y] += size[X]


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n = int(input())
uf = [i for i in range(INT_MAX + 1)]
size = [1 for _ in range(INT_MAX + 1)]

for _ in range(n):
    command = input().split()

    if command[0] == 'I':
        a, b = int(command[1]), int(command[2])
        union(a, b)
    else:
        x = int(command[1])
        print(size[find(x)])
