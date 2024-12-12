import sys

MIN_INT = -sys.maxsize
MAX_INT = sys.maxsize


def find_closest_num(k):
    # 배열을 정렬
    arr.sort()
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')  # 가장 가까운 합
    n1, n2 = 0, 0

    while left < right:
        current_sum = arr[left] + arr[right]

        # 현재 합이 k에 더 가까운지 확인
        if abs(k - current_sum) < abs(k - closest_sum):
            closest_sum = current_sum
            n1, n2 = arr[left], arr[right]

        # 포인터 이동
        if current_sum < k:
            left += 1
        elif current_sum > k:
            right -= 1
        else:  # 정확히 k에 도달하면 바로 반환
            return current_sum, arr[left], arr[right]

    return closest_sum, n1, n2


def parametric_search():
    left, right = MIN_INT, MAX_INT
    closest, n1, n2 = MAX_INT, 0, 0

    while left <= right:
        mid = (left + right) // 2
        closest_num, num1, num2 = find_closest_num(mid)

        if closest_num >= 0:
            right = mid - 1
        else:
            left = mid + 1

        if abs(closest) > abs(closest_num):
            closest, n1, n2 = closest_num, num1, num2

    return n1, n2


n = int(input())
arr = sorted(list(map(int, input().split())))

print(*parametric_search())
