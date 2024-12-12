import sys

MIN_INT = -sys.maxsize
MAX_INT = sys.maxsize


def find_closest_num(k):
    closest, n1, n2 = MAX_INT, 0, 0

    left, right = 0, n - 1
    while left < right:
        if abs(closest - k) > abs(arr[left] + arr[right] - k):
            closest, n1, n2 = arr[left] + arr[right], arr[left], arr[right]

        if arr[left] + arr[right] > k:
            right -= 1
        else:
            left += 1

    return closest, n1, n2


def parametric_search():
    left, right = MIN_INT, MAX_INT
    closest, n1, n2 = MAX_INT, 0, 0

    while left <= right:
        mid = (left + right) // 2
        closest_num, num1, num2 = find_closest_num(mid)

        if closest_num >= 0:
            right = mid - 1
        else:
            left = mid + 1

        if abs(closest) > abs(closest_num):
            closest, n1, n2 = closest_num, num1, num2

    return n1, n2


n = int(input())
arr = sorted(list(map(int, input().split())))

print(*parametric_search())
