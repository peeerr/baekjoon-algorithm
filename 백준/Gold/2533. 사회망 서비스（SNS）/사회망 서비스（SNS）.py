import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(node):
    for v in tree[node]:
        if not visited[v]:
            visited[v] = True
            dfs(v)
            dp[node][0] += dp[v][1]
            dp[node][1] += min(dp[v])


n = int(input())
tree = [[] for _ in range(n + 1)]
dp = [[0, 1] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited[1] = True
dfs(1)

print(min(dp[1]))
