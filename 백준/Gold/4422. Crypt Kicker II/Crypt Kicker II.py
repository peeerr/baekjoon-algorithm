def get(s):
    t = [[] for _ in range(26)]
    n = len(s)
    for i in range(26):
        for j in range(n):
            if s[j] == chr(ord('a') + i):
                t[i].append(j)
    t.sort()
    return t

pt = "the quick brown fox jumps over the lazy dog"
ms = get(pt)
enc = []
rule = {}

while True:
    try:
        s = input()
        enc.append(s)
        if get(s) == ms:
            n = len(s)
            for i in range(n):
                rule[s[i]] = pt[i]
    except EOFError:
        break

if not rule:
    print("No solution.")
else:
    for s in enc:
        decrypted = ''.join(rule.get(char, char) for char in s)
        print(decrypted)
