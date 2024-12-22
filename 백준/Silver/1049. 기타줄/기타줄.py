n, m = map(int, input().split())
packages = []
strings = []

for _ in range(m):
    a, b = map(int, input().split())
    packages.append(a)
    strings.append(b)

packages.sort()
strings.sort()

ans1 = n * strings[0]
ans2 = n // 6 * packages[0] + packages[0]
ans3 = n // 6 * packages[0] + (n % 6 * strings[0])

print(min(ans1, ans2, ans3))
