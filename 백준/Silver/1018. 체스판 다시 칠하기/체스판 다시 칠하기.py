import sys

BOARD_SIZE = 8


n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

ans = sys.maxsize

for i in range(n - BOARD_SIZE + 1):
    for j in range(m - BOARD_SIZE + 1):

        cnt = 0
        for k in range(i, i + BOARD_SIZE):
            for l in range(j, j + BOARD_SIZE):
                if k in [i + 0, i + 2, i + 4, i + 6] and l in [j + 0, j + 2, j + 4, j + 6] and grid[k][l] != 'W':
                    cnt += 1
                elif k in [i + 1, i + 3, i + 5, i + 7] and l in [j + 1, j + 3, j + 5, j + 7] and grid[k][l] != 'W':
                    cnt += 1
                elif k in [i + 0, i + 2, i + 4, i + 6] and l in [j + 1, j + 3, j + 5, j + 7] and grid[k][l] != 'B':
                    cnt += 1
                elif k in [i + 1, i + 3, i + 5, i + 7] and l in [j + 0, j + 2, j + 4, j + 6] and grid[k][l] != 'B':
                    cnt += 1
        ans = min(ans, cnt)

        cnt = 0
        for k in range(i, i + BOARD_SIZE):
            for l in range(j, j + BOARD_SIZE):
                if k in [i + 0, i + 2, i + 4, i + 6] and l in [j + 0, j + 2, j + 4, j + 6] and grid[k][l] != 'B':
                    cnt += 1
                elif k in [i + 1, i + 3, i + 5, i + 7] and l in [j + 1, j + 3, j + 5, j + 7] and grid[k][l] != 'B':
                    cnt += 1
                elif k in [i + 0, i + 2, i + 4, i + 6] and l in [j + 1, j + 3, j + 5, j + 7] and grid[k][l] != 'W':
                    cnt += 1
                elif k in [i + 1, i + 3, i + 5, i + 7] and l in [j + 0, j + 2, j + 4, j + 6] and grid[k][l] != 'W':
                    cnt += 1
        ans = min(ans, cnt)

print(ans)
