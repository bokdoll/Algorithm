# 2020/09/20 (일)
from itertools import combinations


def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1

    mul = 1
    for d in list(dic.values()):
        mul *= (d + 1)
    return mul - 1


if __name__ == '__main__':
    print(solution(clothes=[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))