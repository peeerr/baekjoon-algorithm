t = int(input())

for _ in range(t):
    west_cnt, east_cnt = map(int, input().split())

    dp = [[0 for _ in range(west_cnt + 1)] for _ in range(east_cnt + 1)]

    for i in range(1, east_cnt + 1):
        dp[i][1] = i

    for i in range(2, east_cnt + 1):
        for j in range(2, west_cnt + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    print(dp[east_cnt][west_cnt])
