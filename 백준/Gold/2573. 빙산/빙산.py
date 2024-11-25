from collections import deque


def is_sea(x, y):
    return 0 <= x < n and 0 <= y < m and not grid[x][y]


def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y]


def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for t in range(1, n * m + 1):
    q = deque()
    next_grid = [[0 for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            next_grid[x][y] = grid[x][y]

    for x in range(n):
        for y in range(m):
            if grid[x][y]:
                cnt = 0
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if is_sea(nx, ny):
                        cnt += 1
                if grid[x][y] - cnt < 0:
                    next_grid[x][y] = 0
                else:
                    next_grid[x][y] -= cnt

    for x in range(n):
        for y in range(m):
            grid[x][y] = next_grid[x][y]

    visited = [[False for _ in range(m)] for _ in range(n)]

    cnt = 0
    for x in range(n):
        for y in range(m):
            if can_go(x, y):
                cnt += 1
                visited[x][y] = True
                q.append((x, y))
                bfs()

    if cnt >= 2:
        ans = t
        break

    if cnt == 0:
        ans = 0
        break

print(ans)
