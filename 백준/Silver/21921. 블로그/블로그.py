import sys


def sliding_window():
    start = 0
    sum_val = sum(arr[:k])

    max_sum = sum_val

    for i in range(k, n):
        sum_val -= arr[start]
        sum_val += arr[i]
        start += 1
        max_sum = max(max_sum, sum_val)

    return max_sum


n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = sliding_window()

if not max_sum:
    print('SAD')
    sys.exit(0)
print(max_sum)

start = 0
sum_val = sum(arr[:k])
max_sum_val = sum_val

ans = 1 if max_sum_val == max_sum else 0

for i in range(k, n):
    max_sum_val -= arr[start]
    max_sum_val += arr[i]
    start += 1
    if max_sum_val == max_sum:
        ans += 1

print(ans)
