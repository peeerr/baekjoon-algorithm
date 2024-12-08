n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
idx = 0

ans_arr = []
ans = []

for num in range(1, n + 1):
    if num != arr[idx]:
        stack.append(num)
        ans.append('+')
    else:
        stack.append(num)
        ans.append('+')
        while True:
            if not len(stack):
                break
            top = stack.pop()
            ans_arr.append(top)
            if top != arr[idx]:
                stack.append(top)
                ans_arr.pop()
                break
            ans.append('-')
            idx += 1

if ans_arr == arr:
    for x in ans:
        print(x)
else:
    print('NO')
