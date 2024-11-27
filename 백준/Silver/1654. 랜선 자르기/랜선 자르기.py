import sys

MAX_INT = sys.maxsize


def is_possible(num):
    a = 0
    for x in arr:
        a += x // num
    return a >= n


k, n = map(int, input().split())
arr = sorted([int(input()) for _ in range(k)])

ans = 0
left, right = 1, MAX_INT

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)
