import sys

n = int(sys.stdin.readline())

words = [ sys.stdin.readline().rstrip() for _ in range(n) ]
cnt = 0

for word in words:
    group_word = 1
    lst = []
    for w in word:
        lst.append(word.index(w))

    prev = lst[0]
    for i in lst:
        if i < prev:
            group_word = 0
        prev = i

    if group_word == 1:
        cnt += 1

print(cnt)