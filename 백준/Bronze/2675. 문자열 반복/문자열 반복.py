import sys

t = int(sys.stdin.readline())
for _ in range(t):
    r, s = sys.stdin.readline().split()
    for c in s:
        for _ in range(int(r)):
            print(c, end='')
    print()