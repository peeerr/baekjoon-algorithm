import sys

num1, num2 = sys.stdin.readline().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

print(max(num1, num2))
