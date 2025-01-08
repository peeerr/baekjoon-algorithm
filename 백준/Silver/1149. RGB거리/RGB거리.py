import sys

MAX_INT = sys.maxsize
input = sys.stdin.readline


n = int(input())
rgb = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(3)] for _ in range(n)]

for j in range(3):
    dp[0][j] = rgb[0][j]

for i in range(1, n):
    for j in range(3):
        min_cost = MAX_INT
        for k in range(3):
            if j == k:
                continue
            min_cost = min(min_cost, dp[i - 1][k])
        dp[i][j] = min_cost + rgb[i][j]

print(min(dp[n - 1]))
