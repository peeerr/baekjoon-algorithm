n = int(input())
words = set(input() for _ in range(n))

for x in sorted(words, key=lambda x: (len(x), x)):
    print(x)
