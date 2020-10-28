# 2020/10/18 ()
# [Chapter03-Greedy 예제 4-1] 상하좌우

def solution():
    N = int(input())
    plan = ''.join(input().split())
    curX, curY = 1, 1
    for direction in plan:
        if direction == 'U' and curY != 1:
            curY -= 1
        elif direction == 'D' and curY != N:
            curY += 1
        elif direction == 'L' and curY != 1:
            curX -= 1
        elif direction == 'R' and curY != N:
            curX += 1
    return str(curY) + " " + str(curX)

if __name__ == "__main__":
    print(solution())