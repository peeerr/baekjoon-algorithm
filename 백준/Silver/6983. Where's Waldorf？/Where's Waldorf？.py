T = int(input())
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(T):
    n, m = map(int, input().split())
    grid = [list(input().lower()) for _ in range(n)]
    k = int(input())
    words = [input().lower() for _ in range(k)]

    res = []
    d = dict()

    for x in range(n):
        for y in range(m):
            start = (x, y)
            for i in range(8):
                for word in words:

                    cnt = 0
                    mx, my = x, y
                    com_word = word[0]
                    for w in range(len(word) - 1):
                        if grid[mx][my] == word[w]:
                            nx, ny = mx + dx[i], my + dy[i]
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == word[w + 1]:
                                mx, my = nx, ny
                                cnt += 1
                                com_word += word[w + 1]
                            else:
                                break
                        else:
                            break

                    if cnt == len(word) - 1 and com_word not in d.keys():
                        res.append((start[0] + 1, start[1] + 1))
                        d[com_word] = (start[0] + 1, start[1] + 1)

    for word in words:
        if word in d.keys():
            print(d[word][0], d[word][1])
        else:
            print(n, m)
    print()
