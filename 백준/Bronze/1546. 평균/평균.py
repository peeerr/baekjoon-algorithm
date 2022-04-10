import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
m = max(score)
sum = 0

for i in range(len(score)):
    sum += score[i] / m * 100

print(sum / n)