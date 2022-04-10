import sys

a, b, c = map(int, sys.stdin.readline().split())
same = 0
amount = 1
max = 0

if a == b == c:
    amount = 3
elif a == b or a == c:
    same = a
    amount = 2
elif b == c:
    same = b
    amount = 2

if a > max:
    max = a
if b > max:
    max = b
if c > max:
    max = c

if amount == 3:
    print(10000 + a * 1000)
elif amount == 2:
    print(1000 + same * 100)
elif amount == 1:
    print(max * 100)