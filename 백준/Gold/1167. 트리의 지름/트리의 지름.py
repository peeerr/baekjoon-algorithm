import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(start, diameter):
    global max_v, max_diameter

    if diameter > max_diameter:
        max_v = start
        max_diameter = diameter

    for v, w in tree[start]:
        if not visited[v]:
            visited[v] = True
            dfs(v, diameter + w)


n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n):
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 2, 2):
        tree[info[0]].append((info[i], info[i + 1]))

visited = [False for _ in range(n + 1)]
max_v, max_diameter = 0, 0
visited[1] = True
dfs(1, 0)

visited = [False for _ in range(n + 1)]
start_v = max_v
max_v, max_diameter = 0, 0
visited[start_v] = True
dfs(start_v, 0)

print(max_diameter)
