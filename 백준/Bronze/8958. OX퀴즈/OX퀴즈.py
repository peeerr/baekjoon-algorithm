import sys

n = int(sys.stdin.readline())

for _ in range(n):
    lst = list(sys.stdin.readline())
    score = 0
    count = 1
    for i in lst:
        if i == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)