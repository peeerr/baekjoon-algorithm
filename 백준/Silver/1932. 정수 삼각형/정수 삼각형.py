n = int(input())
triangle = []
triangle += [[int(input())] + [0 for _ in range(n - 1)]]
triangle += [list(map(int, input().split())) + [0 for _ in range(i)] for i in range(n - 2, -1, -1)]

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = triangle[0][0]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + triangle[i][0]

for i in range(1, n):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

print(max(dp[n - 1]))
