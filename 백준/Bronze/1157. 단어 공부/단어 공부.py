import sys

s = sys.stdin.readline().strip().lower()
rm = set(s)
rs = []
dic = {}

for ch in rm:
    dic[ch] = s.count(ch)
    rs.append(s.count(ch))

f = 0
temp = list(dic.values())
temp.remove(max(dic.values()))
for i in temp:
    if i == max(dic.values()):
        f = 1
        break

if f == 1:
    print('?')
else:
    for i in rm:
        if s.count(i) == max(rs):
            print(i.upper())