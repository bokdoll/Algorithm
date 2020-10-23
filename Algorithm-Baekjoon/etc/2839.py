# 2020/10/23 (금)
# 그리디-설탕배달

def solution():
    n = int(input())
    cnt = 0
    while n >= 3:
        if n % 5 != 0:
            n -= 3
            cnt += 1
        else:
            return cnt + n // 5
    if n != 0:
        return -1
    else:
        return cnt



if __name__ == "__main__":
    print(solution())