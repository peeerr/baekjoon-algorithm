import sys, heapq

MAX_INT = sys.maxsize


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

dist = [MAX_INT for _ in range(n + 1)]
dist[start] = 0
pq = [(0, start)]

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if dist[min_idx] != min_dist:
        continue

    for v, w in graph[min_idx]:
        new_dist = min_dist + w
        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))

print(dist[end])
    