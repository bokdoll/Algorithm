# 2020/10/18 (금)
# [Chapter03-Greedy 예제 4-2] 시각

def solution():
    N = int(input())

    # 0~59 중에서 3이 들어가는 횟수 세기
    cnt_sec = 0
    for i in range(60):
        if '3' in str(i):
            cnt_sec += 1

    # 59분동안 3이 들어가는 횟수 : 분에서 3이 들어갈 때 + 들어가지 않을 때
    cnt_min = cnt_sec*60 + (60 - cnt_sec)*cnt_sec

    # 시간마다 cnt_hour에 쌓기
    cnt_hour = 0
    for i in range(N+1):
        if '3' in str(i):
            cnt_hour += 60*60
        else:
            cnt_hour += cnt_min
    return cnt_hour

if __name__ == "__main__":
    print(solution())