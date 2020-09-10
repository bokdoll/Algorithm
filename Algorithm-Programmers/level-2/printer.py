# 2020/09/10 (목)
from collections import deque


def solution(priorities, location):  # 큐 사용
    num = priorities[location]
    priorities[location] = -1
    p = deque(priorities)
    answer = 1

    while True:
        maxP = max(p)
        popped = p.popleft()
        if len(p) == 0:
            return answer
        else:
            if maxP < num:
                if popped == -1:
                    return answer
                else:
                    p.append(popped)
            elif maxP == num:
                if popped == -1:
                    return answer
                else:
                    if popped == maxP:
                        answer += 1
                    else:
                        p.append(popped)
            else:
                if popped < maxP:
                    p.append(popped)
                else:
                    answer += 1


def solution2(priorities, location):    # 실패한 풀이
    num = priorities[location]
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # upperCnt = num 보다 큰 수의 개수
    # lastV = num 보다 큰 수 중 가장 작은 수
    upperCnt, lastV = 0, 0

    for i in range(1, 10):
        nums[i-1] = priorities.count(i)

    for i in range(9, num-1, -1):
        if i > num and nums[i-1] > 0:
            lastV = i

    if lastV == 0:
        return priorities[:location+1].count(num)

    for i in range(num, 9):
        upperCnt += nums[i]

    if priorities.count(num) == 1:
        return upperCnt+1
    else:
        copy = list(reversed(priorities))
        idx = len(priorities) - copy.index(lastV) - 1
        if location < idx:
            return upperCnt + priorities[:location+1].count(num)+priorities[idx+1:].count(num)
        else:
            return upperCnt + priorities[idx+1: location+1].count(num)


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))
