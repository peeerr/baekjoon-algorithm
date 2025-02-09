import sys

MIN_INT = -sys.maxsize


n, k = map(int, input().split())
info = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
dp = [[MIN_INT for _ in range(k + 1)] for _ in range(n + 1)]

dp[0][0] = 0

# i = 현재 고려 중인 보석, j = 무게
# 1. 보석 선택한 경우
# 1-1. dp[i][j] = dp[i - 1][j - weight[i]] + value[i]
# 2. 보석 선택 하지 않은 경우
# 2-1. dp[i][j] = dp[i - 1][j]
for i in range(1, n + 1):
    for j in range(k + 1):
        w, v = info[i][0], info[i][1]
        if j >= w:
            dp[i][j] = dp[i - 1][j - w] + v
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(max(dp[n]))
