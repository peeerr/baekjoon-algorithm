n = int(input())
heights = [0] + list(map(int, input().split()))

stack = []

for i in range(1, n + 1):
    while stack and heights[i] > stack[-1][1]:
        stack.pop()

    if not stack:
        print(0, end=' ')
    else:
        print(stack[-1][0], end=' ')

    stack.append((i, heights[i]))
