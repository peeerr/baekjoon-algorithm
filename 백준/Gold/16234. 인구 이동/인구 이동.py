import sys

input = sys.stdin.readline


def can_go(x, y, num):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and l <= abs(grid[x][y] - num) <= r


def dfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, grid[x][y]):
            alliance.append((nx, ny))
            visited[nx][ny] = True
            dfs(nx, ny)


n, l, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    alliances = []
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            alliance = [(i, j)]
            visited[i][j] = True
            dfs(i, j)
            alliances.append(alliance)

    is_finish = True
    for alliance in alliances:
        if len(alliance) == 1:
            continue
        is_finish = False
        average = sum([grid[x][y] for x, y in alliance]) // len(alliance)
        for x, y in alliance:
            grid[x][y] = average

    if is_finish:
        break
    else:
        ans += 1

print(ans)
