def dfs(start):
    global ans
    for v in graph[start]:
        if not visited[v]:
            ans += 1
            visited[v] = True
            dfs(v)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
visited = [False for _ in range(n + 1)]

visited[1] = True
dfs(1)

print(ans)
