import sys

n = int(sys.stdin.readline())

for i in range(n):
    for _ in range(i+1):
        print('*', end='')
    print()