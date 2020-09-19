# 2020/09/19 (토)

def solution(n):
    lst = [[0]*i for i in range(1, n+1)]
    case = 1
    end = int(n*(n+1)/2)
    x, y = 0, 0 # 현재 좌표

    for i in range(1, end+1):
        lst[x][y] = i
        if case == 1:       # 왼쪽 벽을 타고 내려감 [x+1][y]
            if x == n-1 or lst[x+1][y] != 0:
                case = 2
                y += 1
            else:
                x += 1
        elif case == 2:     # 아래 벽을 타고 오른쪽으로 이동 [x][y+1]
            if y == x or lst[x][y+1] != 0:
                case = 3
                x -= 1
                y -= 1
            else:
                y += 1
        elif case == 3:     # 오른쪽 벽을 타고 올라감 [x-1][y-1]
            if lst[x-1][y-1] != 0:
                case = 1
                x += 1
            else:
                x -= 1
                y -= 1
    answer = []
    for x in lst:
        for ele in x:
            answer.append(ele)
    return answer

if __name__ == '__main__':
    print(solution(n=6))