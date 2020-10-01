# 2020/09/27 (일)

def solution(dartResult):
    curNum = []
    for idx in range(len(dartResult)):
        if ord(dartResult[idx]) >= 48 and ord(dartResult[idx]) <= 57:
            # 10 처리
            if ord(dartResult[idx]) == 48 and idx > 0 and dartResult[idx - 1] == "1":
                curNum[-1] = 10
            else:
                curNum.append(int(dartResult[idx]))
        elif dartResult[idx] == "D":
            curNum[-1] = curNum[-1]**2
        elif dartResult[idx] == "T":
            curNum[-1] = curNum[-1]**3
        elif dartResult[idx] == "*":
            curNum[-1] = curNum[-1]*2
            if idx != 2:
                curNum[-2] = curNum[-2]*2
        elif dartResult[idx] == "#":
            curNum[-1] = curNum[-1]*(-1)
    return sum(curNum)

if __name__ == '__main__':
    print(solution(dartResult='1D2S0T'))