# 2020/11/20 (금)
# [이진 탐색] 나무 자르기
def solution():
    n, m = map(int, input().split())     # n: 나무의 수, m: 높이
    array = list(map(int, input().split()))     # 나무의 높이 리스트

    start, end = 0, max(array)
    mid = (start + end) // 2
    result = 0

    while start != mid and end != mid:
        total = 0
        for h in range(len(array)):
            if array[h] > mid:
                total += array[h]-mid
        if total > m:
            start = mid
            result = mid
        elif total == m:
            return mid
        else:
            end = mid
        mid = (start + end) // 2
    return result


if __name__ == "__main__":
    print(solution())