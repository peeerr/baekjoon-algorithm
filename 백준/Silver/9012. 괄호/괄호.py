T = int(input())

for _ in range(T):
    ps = input()
    stack = []
    is_vpc = True

    for x in ps:
        if x == '(':
            stack.append(x)
        else:
            if not stack:
                is_vpc = False
                break
            stack.pop()

    if not is_vpc or stack:
        print('NO')
    else:
        print('YES')
