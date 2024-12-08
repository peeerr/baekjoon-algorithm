n = int(input())
info = [tuple(map(lambda x : int(x) if x.isdigit() else x, input().split())) for _ in range(n)]

info.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for x in info:
    print(x[0])
