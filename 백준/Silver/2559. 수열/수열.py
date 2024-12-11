n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
sum_val = sum(arr[:k])

ans = sum_val

for i in range(k, n):
    sum_val -= arr[start]
    sum_val += arr[i]
    start += 1
    ans = max(ans, sum_val)

print(ans)
