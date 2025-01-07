import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

for x, y in sorted(points, key=lambda x: (x[0], x[1])):
    print(x, y)
