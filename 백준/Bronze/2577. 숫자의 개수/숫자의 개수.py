import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
lst = list(str(a * b * c))

for i in range(10):
    print(lst.count(str(i)))