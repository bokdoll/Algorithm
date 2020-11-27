# 2020/11/27 (금)
# [Chapter08-다이나믹 프로그래밍] 정수 삼각형


def solution():
    n = int(input())
    array = []
    dp = []
    for i in range(n):
        array.append(list(map(int, input().split())))
        dp.append([0] * (i + 1))    # DP 테이블 초기화
    dp[0][0] = array[0][0]

    for i in range(1, n):  # i : 행
        for j in range(i):  # j : 열
            # 왼쪽 위
            if j == 0:
                up_left = 0
            else:
                up_left = dp[i - 1][j - 1]
            # 오른쪽 위
            if j == i:
                up_right = 0
            else:
                up_right = dp[i - 1][j]
            dp[i][j] = array[i][j] + max(up_left, up_right)

    result = 0
    for i in range(n):
        result = max(result, dp[n - 1][i])
    return result


if __name__ == "__main__":
    print(solution())

'''
5
7
3 8 
8 1 0
2 7 4 4
4 5 2 6 5
'''