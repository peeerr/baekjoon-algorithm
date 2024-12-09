def inorder(i):
    global idx
    if i > n:
        return
    inorder(i * 2)
    tree[i] = inorder_result[idx]
    idx += 1
    inorder(i * 2 + 1)


k = int(input())
n = 2 ** k - 1
inorder_result = list(map(int, input().split()))

tree = [0 for _ in range(n + 1)]
idx = 0
inorder(1)

for i in range(1, k + 1):
    for j in range(2 ** (i - 1), 2 ** i):
        print(tree[j], end=' ')
    print()
