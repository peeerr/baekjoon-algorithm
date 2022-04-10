import sys

c = int(sys.stdin.readline())

for _ in range(c):
    amount = 0
    lst = list(map(int, sys.stdin.readline().split()))
    average = sum(lst[1:]) / lst[0]
    for i in lst[1:]:
        if i > average:
            amount += 1
    result = amount / lst[0] * 100
    print(f"{result:0.3f}%")