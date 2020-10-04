# 2020/10/04 (일)

n = int(input())

for i in range(n):
    score = input()
    sum = 0
    cur = 0
    for s in score:
        if s == 'O':
            cur += 1
            sum += cur
        else:
            cur = 0
    print(sum)