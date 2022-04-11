import sys

s = sys.stdin.readline().strip().upper()
lst = list(set(s))

cnt = []
for i in lst:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(lst[cnt.index(max(cnt))])