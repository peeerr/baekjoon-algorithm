import sys

MIN_INT = -sys.maxsize


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def init():
    for x in range(n):
        for y in range(m):
            explosion_pos[x][y] = False


def put_bomb(time):
    for x in range(n):
        for y in range(m):
            if grid[x][y] == '.':
                grid[x][y] = 'O'
                times[x][y] = time


def explosion(time):
    for x in range(n):
        for y in range(m):
            if times[x][y] == time - 3:
                for dx, dy in zip([0, -1, 1, 0, 0], [0, 0, 0, -1, 1]):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny):
                        explosion_pos[nx][ny] = True

    for x in range(n):
        for y in range(m):
            if explosion_pos[x][y]:
                grid[x][y] = '.'
                times[x][y] = MIN_INT

    init()


n, m, t = map(int, input().split())
grid = [list(input()) for _ in range(n)]
times = [[0 if grid[x][y] == 'O' else MIN_INT for y in range(m)] for x in range(n)]
explosion_pos = [[False for _ in range(m)] for _ in range(n)]

for time in range(2, t + 1):
    put_bomb(time)
    explosion(time)

for row in grid:
    print(''.join(row))
