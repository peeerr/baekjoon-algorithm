import sys
from collections import defaultdict, deque

def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(v, graph, visited):
    q = deque()
    q.append(v)

    while q:
        vertex = q.popleft()
        visited[vertex] = True
        print(vertex, end=' ')

        for i in sorted(graph[vertex]):
            if not visited[i] and i not in q:
                q.append(i)

n, m, v = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = defaultdict(list)
visited = [False] * (n + 1)

for i in g:
    graph[i[0]].append(i[1])
for i in g:
    graph[i[1]].append(i[0])

dfs(v, graph, visited)
visited = [False] * (n + 1)
print()
bfs(v, graph, visited)
