import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().strip()

for i in range(len(b)-1, -1, -1):
    print(a * int(b[i]))
print(a * int(b))