def is_possible(k):
    sum_val = 0
    for x in arr:
        if x > k:
            sum_val += k
        else:
            sum_val += x
    return sum_val <= m


def parametric_search():
    left, right = 1, max(arr)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    return ans


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

print(parametric_search())
