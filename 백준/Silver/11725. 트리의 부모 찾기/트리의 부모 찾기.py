import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(u):
    for v in tree[u]:
        if not visited[v]:
            parents[v] = u
            visited[v] = True
            dfs(v)


n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parents = {}
visited = [False for _ in range(n + 1)]
dfs(1)

for i in range(2, n + 1):
    print(parents[i])
