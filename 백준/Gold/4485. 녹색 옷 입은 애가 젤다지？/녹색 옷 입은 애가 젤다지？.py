import sys, heapq

MAX_INT = sys.maxsize


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for i in range(1, MAX_INT):
    n = int(input())

    if not n:
        break

    grid = [list(map(int, input().split())) for _ in range(n)]
    dist = [[MAX_INT for _ in range(n)] for _ in range(n)]

    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], (0, 0))]

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while pq:
        min_dist, pos = heapq.heappop(pq)
        x, y = pos

        if dist[x][y] != min_dist:
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                new_dist = min_dist + grid[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, (nx, ny)))


    print(f"Problem {i}: {dist[n - 1][n - 1]}")
