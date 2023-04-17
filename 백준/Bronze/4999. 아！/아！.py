import sys

s1 = len(sys.stdin.readline())
s2 = len(sys.stdin.readline())

print("no") if s1 < s2 else print("go")
