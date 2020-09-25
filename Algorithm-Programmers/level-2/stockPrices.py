# 2020/09/20 (일)
# 쉽게 생각하자^^!

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break
    return answer


if __name__ == '__main__':
    print(solution(prices=[1, 2, 3, 2, 3, 1]))
