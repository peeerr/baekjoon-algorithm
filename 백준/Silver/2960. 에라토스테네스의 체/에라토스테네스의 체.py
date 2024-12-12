def simulate():
    cnt = 0
    for i in range(2, n + 1):
        if a[i]:
            for j in range(i, n + 1, i):
                if a[j]:
                    a[j] = False
                    cnt += 1
                    if cnt == k:
                        print(j)
                        return


n, k = map(int, input().split())
a = [True for _ in range(n + 1)]

simulate()
