import sys
n = int(sys.stdin.readline())

result = []
for i in range(n):
    command = sys.stdin.readline()
    lis = command.split()
    if lis[0] == 'push':
        result.append(lis[1])
    elif lis[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif lis[0] == 'size':
        print(len(result))
    elif lis[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif lis[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])