import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(lst[0])
else:
    d = [0] * n
    d[0] = lst[0]
    d[1] = lst[0] + lst[1]
    
    for i in range(2, n):
        d[i] = max(lst[i] + lst[i - 1] + d[i - 3], lst[i] + d[i - 2])

    print(d[-1])
