import sys

sys.setrecursionlimit(10 ** 5)


def dfs(node):
    for v in tree[node]:
        if not visited[v]:
            compliment[v] += compliment[node]
            visited[v] = True
            dfs(v)


n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
compliment = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

root = 0

for i, p in enumerate(list(map(int, input().split())), start=1):
    if p == -1:
        root = i
        continue
    tree[i].append(p)
    tree[p].append(i)

for _ in range(m):
    v, w = map(int, input().split())
    compliment[v] += w

visited[root] = True
dfs(root)

print(*compliment[1:])
