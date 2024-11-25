from collections import deque


def bfs(sx, sy, group_num):
    q = deque([(sx, sy)])
    visited[sx][sy] = group_num
    size = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = group_num
                size += 1
                q.append((nx, ny))
    return size


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
group_size = {}
group_num = 1

for i in range(n):
    for j in range(m):
        if grid[i][j] and not visited[i][j]:
            group_size[group_num] = bfs(i, j, group_num)
            group_num += 1

ans = 0
for i in range(n):
    for j in range(m):
        if not grid[i][j]:
            adj_groups = set()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj]:
                    adj_groups.add(visited[ni][nj])
            size = 1 + sum(group_size[g] for g in adj_groups)
            ans = max(ans, size)

print(ans)
