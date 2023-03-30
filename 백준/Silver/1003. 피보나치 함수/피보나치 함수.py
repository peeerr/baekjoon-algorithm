import sys

fib_count = [[0, 0] for _ in range(41)]
fib_count[0] = [1, 0]
fib_count[1] = [0, 1]

for i in range(2, 41):
    fib_count[i][0] = fib_count[i-1][0] + fib_count[i-2][0]
    fib_count[i][1] = fib_count[i-1][1] + fib_count[i-2][1]

t = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(t)]

for n in lst:
    print(fib_count[n][0], fib_count[n][1])
