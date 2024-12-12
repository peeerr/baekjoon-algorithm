from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    commands = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    # 대괄호 제거([1,2,3,4] -> 1,2,3,4), split으로 바로 나누기
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    # 빈 배열 처리
    if arr[0] != '':
        dq = deque(map(int, arr))
    else:
        dq = deque()

    is_error = False
    reversed_cnt = 0

    for command in commands:
        if command == 'R':
            reversed_cnt += 1
        else:
            if not dq:  # 덱이 비어있는 경우
                is_error = True
                break
            if reversed_cnt % 2 == 1:
                dq.pop()
            else:
                dq.popleft()

    if is_error:
        print('error')
    else:
        if reversed_cnt % 2 == 1:
            dq.reverse()
        print('[' + ','.join(map(str, dq)) + ']')
        