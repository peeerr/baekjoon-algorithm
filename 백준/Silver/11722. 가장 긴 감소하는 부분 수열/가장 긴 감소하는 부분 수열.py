import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

d = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j] and d[j] > d[i] - 1:
            d[i] = d[i] + 1

print(max(d))
