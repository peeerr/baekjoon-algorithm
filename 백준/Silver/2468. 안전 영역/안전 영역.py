import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


def init():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def submerge(height):
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= height:
                grid[i][j] = 0


def can_go(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y] and grid[x][y]


def dfs(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)


def find_cnt():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1
    return cnt


def simulate():
    ans = 0
    for height in range(101):
        init()
        submerge(height)
        ans = max(ans, find_cnt())
    return ans


print(simulate())
