# 2020/10/23 (금)
# 그리디-ATM

def solution():
    n = int(input())    # 사람의 수
    time = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 걸리는 시간

    time.sort()
    answer = 0    # 각 사람이 돈을 인출하는데 필요한 시간의 합
    for i in range(n):
        answer += time[i]*(n-i)
    return answer

if __name__ == "__main__":
    print(solution())