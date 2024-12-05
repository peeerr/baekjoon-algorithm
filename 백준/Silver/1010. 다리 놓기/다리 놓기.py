def factorial(n, cnt):
    ans = 1
    for i in range(cnt):
        ans *= n
        n -= 1
    return ans


t = int(input())

for _ in range(t):
    west_cnt, east_cnt = map(int, input().split())

    top = factorial(east_cnt, west_cnt)
    bottom = factorial(west_cnt, west_cnt)

    print(top // bottom)
