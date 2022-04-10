import sys

n = int(sys.stdin.readline())
result = None
count = 0

if n < 10:
    n *= 10
first = n // 10
second = n % 10

while n != result:
    sum = first + second
    result = (second * 10) + (sum % 10)
    first = result // 10
    second = result % 10
    count += 1

print(count)