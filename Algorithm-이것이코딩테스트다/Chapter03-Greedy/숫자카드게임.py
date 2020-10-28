# 2020/10/16 (금)
# [Chapter03-Greedy 실전문제] 숫자 카드 게임

import sys

def solution():
    lst = list(map(int, sys.stdin.readline().split()))
    N = lst[0]
    answer = []
    for i in range(N):
        lst = list(map(int, sys.stdin.readline().split()))
        answer.append(min(lst))
    return max(answer)



if __name__ == "__main__":
    print(solution())