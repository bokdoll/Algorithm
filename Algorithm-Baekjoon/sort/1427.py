# 2020/11/13 (금)
# 정렬-소트인사이드


def solution():
    n = input()
    nums = [i for i in n]
    return int(''.join(sorted(nums, reverse=True)))


if __name__ == "__main__":
    print(solution())