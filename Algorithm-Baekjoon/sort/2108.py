# 2020/10/23 (금)
# 정렬-통계학
from collections import Counter


def solution():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    nums.sort()

    avg = int(round(sum(nums)/n, 0))

    # 최빈값 구하
    counter = Counter(nums)
    if len(nums) >= 2:
        mode = counter.most_common(n=2)
        if mode[0][1] == mode[1][1]: mode = mode[1][0]
        else: mode = mode[0][0]
    else:
        mode = nums[0]

    return avg, nums[n//2], mode, nums[-1]-nums[0]


if __name__ == "__main__":
    answer = solution()
    for item in answer:
        print(item)