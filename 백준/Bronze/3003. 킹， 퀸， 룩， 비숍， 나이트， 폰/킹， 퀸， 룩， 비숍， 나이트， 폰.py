lst = [1, 1, 2, 2, 2, 8]
ip = list(map(int, input().split()))

for i in range(len(lst)):
    print(f"{lst[i] - ip[i]} ", end='')