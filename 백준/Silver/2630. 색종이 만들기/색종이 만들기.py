def judge(x1, y1, x2, y2):
    global white, blue

    colour = grid[x1][y1]

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if colour != grid[x][y]:
                return False

    if colour:
        blue += 1
    else:
        white += 1

    return True


def backtrack(x1, y1, n):
    if judge(x1, y1, x1 + n - 1, y1 + n - 1):
        return

    n = n // 2
    backtrack(x1, y1, n)  # 좌상
    backtrack(x1, y1 + n, n)  # 우상
    backtrack(x1 + n, y1, n)  # 좌하
    backtrack(x1 + n, y1 + n, n)  # 우하


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

backtrack(0, 0, n)

print(white)
print(blue)
