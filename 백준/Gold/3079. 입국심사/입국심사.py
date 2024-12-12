import sys

MAX_INT = sys.maxsize


def is_possible(time):
    sum_val = 0
    for t in times:
        sum_val += time // t
    return sum_val >= m


def parametric_search():
    left, right = 1, MAX_INT
    ans = MAX_INT

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1

    return ans


n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

print(parametric_search())
