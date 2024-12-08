import sys, heapq

MAX_INT = sys.maxsize


def dijkstra(graph, dist):
    while pq:
        min_dist, min_idx = heapq.heappop(pq)

        if min_dist != dist[min_idx]:
            continue

        for u, w in graph[min_idx]:
            new_dist = min_dist + w
            if new_dist < dist[u]:
                dist[u] = new_dist
                heapq.heappush(pq, (new_dist, u))


n, m, x = map(int, input().split())
forward_graph = [[] for _ in range(n + 1)]
backward_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    forward_graph[u].append((v, w))
    backward_graph[v].append((u, w))

dist_go = [MAX_INT for _ in range(n + 1)]
dist_come = [MAX_INT for _ in range(n + 1)]


pq = [(0, x)]
dist_go[x] = 0
dijkstra(backward_graph, dist_go)

pq = [(0, x)]
dist_come[x] = 0
dijkstra(forward_graph, dist_come)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dist_go[i] + dist_come[i])

print(ans)
