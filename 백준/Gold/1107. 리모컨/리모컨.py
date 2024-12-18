import sys

input = sys.stdin.readline


def is_possible(num):
    for x in list(str(num)):
        if int(x) in impossible:
            return False
    return True


goal = int(input())
m = int(input())
impossible = []
if m:
    impossible = list(map(int, input().split()))

min_press = abs(goal - 100)

for num in range(1000001):
    if is_possible(num):
        min_press = min(min_press, abs(goal - num) + len(str(num)))

print(min_press)
