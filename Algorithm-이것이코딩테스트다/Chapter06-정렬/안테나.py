# 2020/11/13 (금)
# [Chapter06-정렬 24번] 안테나

def solution():
    n = int(input())  # 집의 개수
    location = list(map(int, input().split()))
    location.sort()
    return location[(n-1)//2]


if __name__ == "__main__":
    print(solution())

'''
4
5 1 7 9
'''