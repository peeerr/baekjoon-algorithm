import sys

n = int(sys.stdin.readline())
result = n
count = 0

while True:
    first = result // 10
    second = result % 10
    num = (first + second) % 10
    result = (second * 10) + num
    count += 1
    if(result == n):
        break

print(count)