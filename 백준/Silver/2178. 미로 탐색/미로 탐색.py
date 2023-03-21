import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n) ]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append( (x, y) )

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not (nx == 0 and ny == 0):  # 시작 정점은 제외
                graph[nx][ny] = graph[x][y] + 1
                queue.append( (nx, ny) )

    return graph[n - 1][m - 1]

print(bfs(0, 0))