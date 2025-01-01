n, m = map(int, input().split())
passwords = {}

for _ in range(n):
    site, password = input().split()
    passwords[site] = password

for _ in range(m):
    site = input()
    print(passwords[site])
