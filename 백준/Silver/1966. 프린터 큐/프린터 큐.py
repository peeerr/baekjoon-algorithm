from collections import deque


def can_printing(num):
    for i in range(len(dq)):
        if num < dq[i][1]:
            return False
    return True


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    dq = deque()

    for idx, item in enumerate(list(map(int, input().split()))):
        dq.append((idx, item))

    ans, cnt = 0, 0

    while True:
        idx, num = dq.popleft()
        if can_printing(num):
            cnt += 1
            if idx == m:
                print(cnt)
                break
        else:
            dq.append((idx, num))
