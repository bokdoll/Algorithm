# 2020/09/10 (목)
def solution(numbers, hand):
    # 2차원 배열
    keypad = [0, (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),
              (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
    # 1. 똑같은 키패드 배열 복사
    answer = numbers[:]
    hand = hand.upper()[0]

    # 왼손, 오른손이 현재 있는 위치를 표현
    lastL, lastR = 10, 12

    for idx, e in enumerate(numbers):
        if e == 0:
            e = 11
        # 2-1. 왼쪽에 있는 키패드(1, 4, 7) -> L로 변경
        if e in (1, 4, 7):
            answer[idx] = 'L'
            lastL = e
        # 2-2. 오른쪽에 있는 키패드(3, 6, 9) => R로 변경
        elif e in (3, 6, 9):
            answer[idx] = 'R'
            lastR = e
        # 2-3. 거리를 참고하여 손 선택.
        else:
            distL = abs(keypad[e][0] - keypad[lastL][0]) + \
                abs(keypad[e][1] - keypad[lastL][1])
            distR = abs(keypad[e][0] - keypad[lastR][0]) + \
                abs(keypad[e][1] - keypad[lastR][1])
            if (distL > distR):
                answer[idx] = 'R'
                lastR = e
            elif (distL == distR):
                answer[idx] = hand
                if (hand == 'L'):
                    lastL = e
                else:
                    lastR = e
            else:
                answer[idx] = 'L'
                lastL = e
    return ''.join(answer)


if __name__ == '__main__':
    numbers = [2, 8, 5, 0, 2, 8, 8, 5, 0, 0, 2, 0]
    hand = "left"
    print(solution(numbers, hand))
