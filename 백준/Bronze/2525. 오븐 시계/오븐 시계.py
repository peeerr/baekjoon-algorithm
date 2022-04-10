import sys

hour, minute = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

hour = hour + ((minute + time) // 60)
minute = (minute + time) % 60

if hour >= 24:
    print(hour - 24, minute)
else:
    print(hour, minute)