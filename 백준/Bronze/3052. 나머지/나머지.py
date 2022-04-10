import sys

lst = []
for i in range(10):
    lst.append(int(sys.stdin.readline()) % 42)

print(len(set(lst)))