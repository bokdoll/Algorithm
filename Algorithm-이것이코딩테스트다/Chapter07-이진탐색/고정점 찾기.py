# 2020/11/19 (목)
# [Chapter07-이진 탐색] 고정점 찾기


def solution():
    n = int(input())
    array = list(map(int, input().split()))

    start, end = 0, n-1

    while start <= end:
        mid = (start + end) // 2
        if mid == array[mid]:
            return mid
        if start == mid or end == mid:
            return -1
        if mid > array[mid]:
            start = mid
        elif mid < array[mid]:
            end = mid


if __name__ == "__main__":
    print(solution())

'''
5
-15 -6 1 3 7
'''
'''
7
-15 -4 2 8 9 13 15
'''
'''
7
-15 -4 3 8 9 13 15
'''