# 2020/11/19 (목)
# [Chapter07-이진 탐색] 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right


def solution():
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    count = count_by_range(array, left_value=x, right_value=x)
    if count == 0:
        return -1
    else:
        return count


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


if __name__ == "__main__":
    print(solution())

'''
7 2
1 1 2 2 2 2 3
'''

'''
7 4
1 1 2 2 2 2 3
'''