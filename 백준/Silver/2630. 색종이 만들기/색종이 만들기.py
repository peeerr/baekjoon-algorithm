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


def simulate(x, y, n):
    if judge(x, y, x + n - 1, y + n - 1):
        return

    n = n // 2
    simulate(x, y, n)  # 좌상
    simulate(x, y + n, n)  # 우상
    simulate(x + n, y, n)  # 좌하
    simulate(x + n, y + n, n)  # 우하


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

simulate(0, 0, n)

print(white)
print(blue)
