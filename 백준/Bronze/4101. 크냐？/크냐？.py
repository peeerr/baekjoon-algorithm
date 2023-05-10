a, b = map(int, input().split())

while a:
    if a > b:
        print("Yes")
    else:
        print("No")
    a, b = map(int, input().split())
    