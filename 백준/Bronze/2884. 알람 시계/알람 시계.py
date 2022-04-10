import sys

hour, minute = map(int, sys.stdin.readline().split())

if minute >= 45:
    print(hour, minute-45)
elif hour == 0 and minute < 45:
    print(23, minute+15)
else:
    print(hour-1, minute+15)