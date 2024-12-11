from collections import defaultdict


def can_make():
    for s in ['A', 'C', 'G', 'T']:
        if s_cnt[s] < dna_cnt[s]:
            return False
    return True


n, k = map(int, input().split())
arr = list(input())

dna_cnt = {}
s_cnt = defaultdict(int)

for s, c in zip(['A', 'C', 'G', 'T'], map(int, input().split())):
    dna_cnt[s] = c

for i in range(k):
    s_cnt[arr[i]] += 1

ans = 1 if can_make() else 0
start = 0

for i in range(k, n):
    s_cnt[arr[start]] -= 1
    s_cnt[arr[i]] += 1
    start += 1
    if can_make():
        ans += 1

print(ans)
