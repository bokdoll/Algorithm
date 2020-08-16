def solution(N, stages):
    users, errorRate, answer = {}, {}, []
    for i in range(1, N + 2):
        users[i] = 0

    for s in stages:
        users[s] += 1

    reached = sum(list(users.values()))
    for i in range(1, N+1):
        # 분모가 0일 떄 처리
        if reached != 0:
            errorRate[i] = users[i]/reached
        else:
            errorRate[i] = 0
        reached -= users[i]

    # 딕셔너리 value로 정렬
    errorRate = sorted(errorRate.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for stage in errorRate:
        answer.append(stage[0])
    print(answer)
    return answer


if __name__ == '__main__':
    stages = [1, 2, 3, 4, 5, 6, 7]
    N = 8
    solution(N, stages)