import sys

input = sys.stdin.readline

s = input()

res = '0' * (s.count('0') // 2)
res += '1' * (s.count('1') // 2)

print(res)
