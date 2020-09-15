# 2020/09/15 (화)
from itertools import combinations

def solution(numbers):
    numbers.sort()
    return list(set([t[0] + t[1] for t in list(combinations(numbers, 2))]))

if __name__ == '__main__':
    numbers = [0,1, 0, -1,1,0]
    print(solution(numbers))