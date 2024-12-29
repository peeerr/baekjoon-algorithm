n = int(input())

if n:
    scores = sorted([int(input()) for _ in range(n)])
    except_n = int(n * 0.15 + 0.5)
    print(int(sum(scores[except_n:n - except_n]) / (n - except_n * 2) + 0.5))
else:
    print(0)
