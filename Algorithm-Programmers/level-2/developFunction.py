# 2020/09/10 (목)
import math
from collections import deque


def solution(progresses, speeds):
    restDays, cnt = deque(), []

    # 작업이 남은 날 구하기
    for p, s in zip(progresses, speeds):
        restDays.append(math.ceil((100-p)/s))

    # restDay를 훑으며 큰 수들을 maxD로 정의하고 그 뒤 maxD보다 작은 수의 개수(c)를 count
    maxD, c = restDays[0], 0
    while len(restDays) >= 0:
        if len(restDays) == 0:
            cnt.append(c)
            break
        popped = restDays.popleft()
        if popped <= maxD:
            c += 1
        else:
            cnt.append(c)
            maxD, c = popped, 1
    return cnt


if __name__ == '__main__':
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))
