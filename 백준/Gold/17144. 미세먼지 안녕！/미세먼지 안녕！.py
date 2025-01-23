n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] != -1


def spread():
    next_grid = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            next_grid[x][y] = grid[x][y]

    for x in range(n):
        for y in range(m):
            if grid[x][y] <= 0:
                continue
            cnt = 0
            spread_amo = grid[x][y] // 5
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if can_go(nx, ny):
                    next_grid[nx][ny] += spread_amo
                    cnt += 1
            next_grid[x][y] -= spread_amo * cnt

    for x in range(n):
        for y in range(m):
            grid[x][y] = next_grid[x][y]


def find_air_cleaner():
    for x in range(n):
        if grid[x][0] == -1:
            return x, x + 1


def up_cleaning(top):
    # 반시계 방향 회전
    # 오른쪽 이동 (공기청정기 옆부터 시작)
    tmp = grid[top][m - 1]
    for y in range(m - 1, 1, -1):
        grid[top][y] = grid[top][y - 1]
    grid[top][1] = 0

    # 위쪽 이동 (오른쪽 끝 상단으로)
    tmp2 = grid[0][m - 1]
    for x in range(top - 1):
        grid[x][m - 1] = grid[x + 1][m - 1]
    grid[top - 1][m - 1] = tmp

    # 왼쪽 이동 (왼쪽 끝으로)
    tmp3 = grid[0][0]
    for y in range(m - 1):
        grid[0][y] = grid[0][y + 1]
    grid[0][m - 2] = tmp2

    # 아래쪽 이동 (공기청정기 위로)
    for x in range(top - 1, 1, -1):
        grid[x][0] = grid[x - 1][0]
    grid[1][0] = tmp3


def down_cleaning(bottom):
    # 시계 방향 회전
    tmp = grid[bottom][m - 1]
    for y in range(m - 1, 1, -1):
        grid[bottom][y] = grid[bottom][y - 1]
    grid[bottom][1] = 0

    tmp2 = grid[n - 1][m - 1]
    for x in range(n - 1, bottom + 1, -1):
        grid[x][m - 1] = grid[x - 1][m - 1]
    grid[bottom + 1][m - 1] = tmp

    tmp3 = grid[n - 1][0]
    for y in range(m - 1):
        grid[n - 1][y] = grid[n - 1][y + 1]
    grid[n - 1][m - 2] = tmp2

    for x in range(bottom + 1, n - 1):
        grid[x][0] = grid[x + 1][0]
    grid[n - 2][0] = tmp3


def air_cleaning():
    top, bottom = find_air_cleaner()
    up_cleaning(top)
    down_cleaning(bottom)


def check_dust():
    return sum(sum(filter(lambda x: x > 0, row)) for row in grid)


def simulate():
    for _ in range(t):
        spread()
        air_cleaning()
    return check_dust()


print(simulate())
