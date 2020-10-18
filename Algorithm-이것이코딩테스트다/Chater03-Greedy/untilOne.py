# 2020/10/18 ()
# [Chapter03-Greedy 실전문제] 1이 될 때까지

def solution():
    N, K = map(int, input().split())
    cnt = 0
    while N > 1:
        cnt += 1
        if N % K == 0:
            N /= K
        else:
            N -= 1

    return cnt

if __name__ == "__main__":
    print(solution())