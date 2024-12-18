n, m = map(int, input().split())
d = {}

for i, name in enumerate([input() for _ in range(n)], start=1):
    d[str(i)] = name
    d[name] = i

for _ in range(m):
    keyword = input()
    print(d[keyword])
