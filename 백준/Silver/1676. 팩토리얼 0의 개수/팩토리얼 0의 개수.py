n = int(input())

ans = 0
while n >= 5:
    ans += n // 5
    n //= 5

print(ans)
