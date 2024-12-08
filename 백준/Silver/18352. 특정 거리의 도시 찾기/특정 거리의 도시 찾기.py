from collections import deque


def bfs():
    while q:
        v = q.popleft()

        for u in graph[v]:
            if not visited[u]:
                dist[u] = dist[v] + 1
                visited[u] = True
                q.append(u)


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

q = deque([x])
visited = [False for _ in range(n + 1)]
visited[x] = True

bfs()

nothing = True
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        nothing = False

if nothing:
    print(-1)
