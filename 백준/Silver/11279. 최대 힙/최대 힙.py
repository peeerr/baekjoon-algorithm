import sys, heapq

input = sys.stdin.readline


n = int(input())
pq = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(pq, -x)
    else:
        try:
            print(-heapq.heappop(pq))
        except IndexError:
            print(0)
