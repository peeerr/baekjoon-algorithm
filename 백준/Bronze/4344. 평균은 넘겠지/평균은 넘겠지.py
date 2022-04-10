import sys

c = int(sys.stdin.readline())

for _ in range(c):
    sum = 0
    amount = 0
    lst = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(lst)):
        sum += lst[i]
    average = sum / lst[0]
    for i in range(1, len(lst)):
        if lst[i] > average:
            amount += 1
    result = amount / lst[0] * 100
    print(f"{result:0.3f}%")