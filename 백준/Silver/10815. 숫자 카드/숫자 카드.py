n = int(input())
cards = set(input().split())
m = int(input())

for x in input().split():
    if x in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
