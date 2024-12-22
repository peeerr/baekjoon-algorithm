import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
out = [[False for _ in range(m)] for _ in range(n)]


def is_all_melted():
    for x in range(n):
        for y in range(m):
            if grid[x][y]:
                return False
    return True


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    return in_range(x, y) and not out[x][y] and not grid[x][y]


def is_out(x, y):
    return in_range(x, y) and out[x][y]


def init():
    for x in range(n):
        for y in range(m):
            out[x][y] = False


def find_out(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            out[nx][ny] = True
            find_out(nx, ny)


def find_cheeses_cnt():
    cnt = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y]:
                cnt += 1
    return cnt


def find_should_melted_cheeses():
    should_melted_cheeses = []
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for x in range(n):
        for y in range(m):
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if is_out(nx, ny):
                    should_melted_cheeses.append((x, y))

    return should_melted_cheeses


def melt():
    init()
    find_out(0, 0)

    for x, y in find_should_melted_cheeses():
        grid[x][y] = 0


def simulate():
    for time in range(1, n):
        cnt = find_cheeses_cnt()
        melt()
        if is_all_melted():
            return time, cnt


for x in simulate():
    print(x)
