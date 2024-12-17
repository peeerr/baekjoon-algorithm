n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    max_num, max_idx = -1, -1
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > max_num:
            max_num, max_idx = dp[j], j
    if max_idx != -1:
        dp[i] = max_num + 1

print(max(dp))
