MAX_INT = 100000

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
counting = [0 for _ in range(MAX_INT + 1)]

ans, j = 0, 0

for i in range(1, n + 1):
    while j + 1 <= n and counting[arr[j + 1]] != k:
        counting[arr[j + 1]] += 1
        j += 1

    ans = max(ans, j - i + 1)
    counting[arr[i]] -= 1

print(ans)
