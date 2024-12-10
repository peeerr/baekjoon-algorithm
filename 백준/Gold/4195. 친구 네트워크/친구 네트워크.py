import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INT_MAX = 1000000


def mapping(x):
    global idx

    if x in mapper:
        x = mapper[x]
    else:
        mapper[x] = idx
        x = idx
        idx += 1

    return x


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


T = int(input())

for _ in range(T):
    uf = [i for i in range(INT_MAX + 1)]
    size = [1 for _ in range(INT_MAX + 1)]
    mapper = {}
    idx = 1

    for _ in range(int(input())):
        a, b = map(lambda x: mapping(x), input().split())
        union(a, b)
        parent = find(a)
        print(size[parent])
