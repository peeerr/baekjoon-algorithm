numbers = set(range(1, 10001))
rm = set()

for i in numbers:
    for j in str(i):
        i += int(j)
    if i <= 100000:
        rm.add(i)

result = numbers - rm
for i in sorted(result):
    print(i)