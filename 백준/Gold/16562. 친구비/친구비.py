import sys

INT_MAX = sys.maxsize


def union(x, y):
    global ans
    X, Y = find(x), find(y)
    if X != Y:
        uf[X] = Y
        dp[Y] = min(dp[Y], dp[X])


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
uf = [i for i in range(n + 1)]
dp = cost[:]

ans = INT_MAX

for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

friends = set()
ans = 0

for i in range(1, n + 1):
    parent = find(i)
    if parent not in friends:
        ans += dp[parent]
        friends.add(parent)

print(ans if ans <= k else 'Oh no')
