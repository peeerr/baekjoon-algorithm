n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = min(price[:n-2])
ans = 0

for i in range(n - 1):
    if price[i] == min_price:
        ans += min_price * sum(distance[i:])
        break
    else:
        ans += price[i] * distance[i]

print(ans)
