# 2020/11/27 (금)
# [Chapter08-다이나믹 프로그래밍 실전문제] 개미 전사

def solution():
    n = int(input()) # n : 식량 창고의 개수
    array = list(map(int, input().split())) # 각 식량차고에 저장된 식량의 개수

    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 100

    # 다이나믹 프로그래밍 진행(bottom up)
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])
    return d[n-1]


if __name__ == "__main__":
    print(solution())

'''
4
1 3 1 5
'''