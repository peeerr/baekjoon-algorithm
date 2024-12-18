from collections import deque


def bfs():
    while q:
        curr, cnt = q.popleft()

        if curr == k:
            return cnt

        if curr - 1 >= 0 and not visited[curr - 1]:
            q.append((curr - 1, cnt + 1))
            visited[curr - 1] = True

        if curr + 1 <= 100000 and not visited[curr + 1]:
            q.append((curr + 1, cnt + 1))
            visited[curr + 1] = True

        if curr * 2 <= 100000 and not visited[curr * 2]:
            q.append((curr * 2, cnt + 1))
            visited[curr * 2] = True


n, k = map(int, input().split())
visited = [False for _ in range(100001)]

q = deque([(n, 0)])
visited[n] = True

print(bfs())
