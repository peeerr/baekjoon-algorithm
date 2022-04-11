import sys

def sq(n):
    s = str(n)
    for i in range(len(s)-2):
        d = int(s[i + 1]) - int(s[i])
        if d != int(s[i+2]) - int(s[i+1]):
            return 0  # 한수가 아니면 0 반환
        d = int(s[i+1]) - int(s[i])
    return 1  # 한수면 1 반환

max = int(sys.stdin.readline())
amount = 0
for i in range(1, max+1):
    amount += sq(i)

print(amount)