import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(lst)
res = 0

while start <= end:
    mid = (start + end) // 2
    sum_tree = 0

    for i in lst:
        if i > mid:
            sum_tree += i - mid

    if sum_tree >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
