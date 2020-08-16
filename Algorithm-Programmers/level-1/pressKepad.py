# 2020/08/16 (일)
def solution(numbers, hand):
    # 1. 똑같은 키패드 배열 복사
    answer = numbers[:]
    hand = hand.upper()[0]

    # 왼손, 오른손이 현재 있는 위치를 표현
    lastL, lastR = 10, 12

    for idx, e in enumerate(numbers):
        print(idx, lastR, lastL)
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
        # 3. 앞의 R, L을 참고하여 선택
        else:
            if lastL == 10 and lastR == 12:
                answer[idx] = hand
                _, lastL, lastR = checkHand(e, lastL, lastR, hand)
                continue
            elif lastL == 10 or lastR == 12:
                distL, distR = abs(lastL - e), abs(lastR - e)
                answer[idx], lastL, lastR = checkLR(e, distL, distR, lastL, lastR, hand, False)
            else:
                distL, distR = abs(lastL - e), abs(lastR - e)
                # answer[idx], lastL, lastR = checkLR(e, distL, distR, lastL, lastR, hand, True)
                if lastL in (0, 2, 5, 8, 11) and lastL != e:
                    distL = int(distL/3)
                if lastR in (0, 2, 5, 8, 11) and lastR != e:
                    distR = int(distR/3)
                if distL < distR:
                    answer[idx] = 'L'
                    lastL = e
                elif distL == distR:
                    answer[idx] = hand
                    if hand == 'R':
                        lastR = e
                    else:
                        lastL = e
                else:
                    if distL-2 == distR and lastL not in (2, 5, 8, 11) and lastR not in (2, 5, 8, 11):
                        answer[idx] = hand
                        if hand == 'R':
                            lastR = e
                        else:
                            lastL = e
                    else:
                        answer[idx] = 'R'
                        lastR = e

    print(numbers)
    print(''.join(answer))
    return ''.join(answer)


def checkLR(val, distL, distR, lastL, lastR, hand, isCenter):
    if isCenter:
        if lastL in (0, 2, 5, 8, 11) and lastL != val:
            distL = int(distL / 3)
        if lastR in (0, 2, 5, 8, 11) and lastR != val:
            distR = int(distR / 3)
    if distL < distR:
        return 'L', val, lastR
    elif distL == distR:
        return checkHand(val, lastL, lastR, hand)
    else:
        if isCenter:
            if distL-2 == distR and lastL not in (2, 5, 8, 11) and lastR not in (2, 5, 8, 11):
                return checkHand(val, lastL, lastR, hand)
        return 'R', lastL, val


def checkHand(val, lastL, lastR, hand):
    if hand == 'R':
        return hand, lastL, val
    else:
        return hand, val, lastR


if __name__ == '__main__':
    numbers = [2, 8, 5, 0, 2, 8, 8, 5, 0, 0, 2, 0]
    hand = "left"
    solution(numbers, hand)
