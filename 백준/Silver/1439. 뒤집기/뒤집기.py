s = input()

prev = s[0]
group_count = {'0': 0, '1': 0}
group_count[prev] += 1

for n in s:
    if n != prev:
        group_count[n] += 1
        prev = n

print(min(group_count.values()))
