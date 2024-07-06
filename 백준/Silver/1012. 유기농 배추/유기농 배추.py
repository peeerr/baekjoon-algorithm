T = int(input())


def in_range(y, x):
    return 0 <= x < m and 0 <= y < n


def dfs(y, x):
    if in_range(y, x) and grid[y][x] == 1:
        grid[y][x] = 0

        dfs(y, x - 1)
        dfs(y + 1, x)
        dfs(y, x + 1)
        dfs(y - 1, x)


for _ in range(T):
    m, n, k = map(int, input().split())

    grid = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1

    cnt = 0
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 1:
                dfs(y, x)
                cnt += 1

    print(cnt)
