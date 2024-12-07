import heapq, sys

MAX_INT = sys.maxsize


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

a, b = map(int, input().split())
pq = [(0, a)]
dist = [MAX_INT for _ in range(n + 1)]
dist[a] = 0

path = [0 for _ in range(n + 1)]

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if min_dist != dist[min_idx]:
        continue

    for u, w in graph[min_idx]:
        new_dist = min_dist + w
        if new_dist < dist[u]:
            dist[u] = new_dist
            heapq.heappush(pq, (new_dist, u))
            path[u] = min_idx

print(dist[b])

curr_v = b
ans = [curr_v]

while curr_v != a:
    curr_v = path[curr_v]
    ans.append(curr_v)

print(len(ans))
print(*ans[::-1])
