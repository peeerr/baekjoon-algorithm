def pre_order(node):
    if node == '.':
        return
    print(node, end='')
    pre_order(left[node])
    pre_order(right[node])


def in_order(node):
    if node == '.':
        return
    in_order(left[node])
    print(node, end='')
    in_order(right[node])


def post_order(node):
    if node == '.':
        return
    post_order(left[node])
    post_order(right[node])
    print(node, end='')


n = int(input())
left, right = {}, {}

for _ in range(n):
    parent, left_child, right_child = input().split()
    left[parent] = left_child
    right[parent] = right_child

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()
