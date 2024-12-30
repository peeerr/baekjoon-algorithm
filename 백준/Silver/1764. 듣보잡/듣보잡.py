n, m = map(int, input().split())

if n >= m:
    g = set([input() for _ in range(n)])
    l = set([input() for _ in range(m)])
else:
    l = set([input() for _ in range(m)])
    g = set([input() for _ in range(n)])

cnt = 0
people = []

for x in l:
    if x in g:
        cnt += 1
        people.append(x)

print(cnt)

for x in sorted(people):
    print(x)
