import sys
from collections import deque

input = sys.stdin.readline
dq = deque([i for i in range(1, int(input()) + 1)])

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
