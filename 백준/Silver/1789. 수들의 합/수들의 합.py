import sys

input = sys.stdin.readline

S = int(input())
sum = 0
cnt = 0

for i in range(1, S + 1):
    sum += i
    if sum > S:
        break
    cnt += 1

print(cnt)
