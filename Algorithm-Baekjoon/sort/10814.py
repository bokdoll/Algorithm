# 2020/11/13 (금)
# 정렬-나이순 정렬
import sys


def solution():
    n = int(input())
    member = []
    for i in range(n):
        member.append(list(sys.stdin.readline().split()))
        member[i][0] = int(member[i][0])
    return sorted(member, key=lambda x: x[0])


if __name__ == "__main__":
    answer = solution()
    for item in answer:
        print(int(item[0]), item[1])