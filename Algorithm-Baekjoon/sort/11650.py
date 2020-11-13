# 2020/11/13 (금)
# 정렬-좌표 정렬하기
import sys


def solution():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(list(map(int, sys.stdin.readline().split())))
    return sorted(nums, key=lambda x: (x[0], x[1]))


if __name__ == "__main__":
    answer = solution()
    for item in answer:
        print(item[0], item[1])