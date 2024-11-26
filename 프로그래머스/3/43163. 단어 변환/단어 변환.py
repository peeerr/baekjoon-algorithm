from collections import deque


def solution(begin, target, words):
    visited = set([begin])
    q = deque([(begin, 0)])
    
    while q:
        begin, cnt = q.popleft()
        
        if begin == target:
            return cnt
        
        for word in words:
            for i in range(len(word)):
                s = begin[0:i] + word[i] + begin[i+1:]
                if s in words and s not in visited:
                    q.append((s, cnt + 1))
                    visited.add(s)
            
    return 0
