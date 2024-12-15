import sys

sys.setrecursionlimit(10000)


def dfs(node):
    for v in tree[node]:
        if not visited[v]:
            visited[v] = True
            dfs(v)

    dp[node][0], dp[node][1] = 0, weight[node]

    for v in tree[node]:
        dp[node][0] += max(dp[v])
        dp[node][1] += dp[v][0]


n = int(input())
weight = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

visited[1] = True
dfs(1)

print(max(dp[1]))
