# 2020/11/27 (금)
# [Chapter08-다이나믹 프로그래밍] 금광

def solution():
    for tc in range(int(input())):
        n, m = map(int, input().split())
        array = list(map(int, input().split()))

        # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
        dp = []
        index = 0
        for i in range(n):
            dp.append(array[index:index + m])
            index += m
        # 다이나믹 프로그래밍 진행
        for j in range(1, m):
            for i in range(n):
                # 왼쪽 위에서 오는 경우
                if i == 0:
                    left_up = 0
                else:
                    left_up = dp[i - 1][j - 1]
                # 왼쪽 아래에서 오는 경우
                if i == n - 1:
                    left_down = 0
                else:
                    left_down = dp[i + 1][j - 1]
                # 왼쪽에서 오는 경우
                left = dp[i][j - 1]
                dp[i][j] = dp[i][j] + max(left_up, left_down, left)
        result = 0
        for i in range(n):
            result = max(result, dp[i][m-1])
        print(result)


if __name__ == "__main__":
    solution()


'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4 
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2 
'''