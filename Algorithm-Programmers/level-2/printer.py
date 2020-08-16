def solution(priorities, location):
    num = priorities[location]
    nums = {}

    # upperCnt = num보다 큰 수의 개수
    # lastV = num보다 큰 수 중 가장 작은 수
    upperCnt, lastV = 0, 0

    for i in range(1, 10):
        nums[i] = priorities.count(i)

    for i in range(9, num-1, -1):
        if i > num and nums[i] > 0:
            lastV = i
    print(lastV)

    if lastV == 0:
        return priorities[:location+1].count(num)

    for i in range(num, 9):
        upperCnt += list(nums.items())[i][1]
    print(upperCnt)

    if priorities.count(num) == 1:
        return upperCnt+1
    else:
        copy = list(reversed(priorities))
        idx = len(priorities) - copy.index(lastV) - 1
        print(idx)
        if location < idx:
            return upperCnt + priorities[:location+1].count(num)+priorities[idx:].count(num)
        else:
            return upperCnt + priorities[idx: location+1].count(num)


if __name__ == '__main__':
    priorities = [1, 2, 3, 2]
    location = 3
    print(solution(priorities, location))