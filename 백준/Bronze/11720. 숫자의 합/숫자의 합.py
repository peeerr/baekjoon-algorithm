import sys

n = sys.stdin.readline()
num = sys.stdin.readline().strip()
sum = 0

for i in num:
    sum += int(i)
print(sum)