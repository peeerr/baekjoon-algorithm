n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    
    date = i + t[i] - 1
    if date <= n:
        dp[date] = max(dp[date], dp[i - 1] + p[i])
        
print(max(dp))
