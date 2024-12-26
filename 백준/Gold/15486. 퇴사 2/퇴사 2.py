import sys

input = sys.stdin.readline


n = int(input())
info = [0] + [tuple(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n + 1)]
max_p = 0  # 현재까지의 최대 수익

for i in range(1, n + 1):
    # 이전까지의 최대 수익 갱신
    max_p = max(max_p, dp[i - 1])

    t, p = info[i]
    if i + t > n + 1:
        continue

    # i일에 상담을 하는 경우의 수익 = 현재까지 최대 수익 + 현재 상담 수익
    dp[i + t - 1] = max(dp[i + t - 1], max_p + p)

print(max(dp))
