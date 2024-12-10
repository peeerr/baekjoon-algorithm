def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n = int(input())
m = int(input())

uf = [i for i in range(n + 1)]

for i in range(1, n + 1):
    x = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if x[j]:
            union(i, j)

path = list(map(int, input().split()))
is_possible = True

for i in range(m - 1):
    if find(path[i]) != find(path[i + 1]):
        is_possible = False

if is_possible:
    print('YES')
else:
    print('NO')
