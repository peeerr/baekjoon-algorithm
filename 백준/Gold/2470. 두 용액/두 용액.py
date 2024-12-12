import sys

MAX_INT = sys.maxsize


n = int(input())
arr = sorted(list(map(int, input().split())))

closest, n1, n2 = MAX_INT, 0, 0

left, right = 0, n - 1
while left < right:
    if abs(closest) > abs(arr[left] + arr[right]):
        closest, n1, n2 = arr[left] + arr[right], arr[left], arr[right]

    if arr[left] + arr[right] > 0:
        right -= 1
    else:
        left += 1

print(n1, n2)
