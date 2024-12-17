import sys

input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def get_cnt():
    max_cnt = 0

    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if grid[i][j] == grid[i][j + 1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)

    for j in range(n):
        cnt = 1
        for i in range(n - 1):
            if grid[i][j] == grid[i + 1][j]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt


n = int(input())
grid = [list(input()) for _ in range(n)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for x in range(n):
    for y in range(n):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] != grid[x][y]:
                grid[nx][ny], grid[x][y] = grid[x][y], grid[nx][ny]
                ans = max(ans, get_cnt())
                grid[nx][ny], grid[x][y] = grid[x][y], grid[nx][ny]

print(ans)
