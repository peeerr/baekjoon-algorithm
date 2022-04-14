import sys

s = sys.stdin.readline().split()
s[0] = "".join(reversed(s[0]))
s[1] = "".join(reversed(s[1]))

print(max(s))