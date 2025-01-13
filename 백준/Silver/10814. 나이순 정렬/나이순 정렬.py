n = int(input())
people = [[i] + list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for i in range(n)]

for _, age, name in sorted(people, key=lambda x: (x[1], x[0])):
    print(age, name)
