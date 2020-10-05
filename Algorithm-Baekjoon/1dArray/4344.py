# 2020/10/05 (월)

c = int(input())
for i in range(c):
    lst = list(map(int, input().split()))
    num = lst[0]
    avg = sum(lst[1:])/num
    overN = 0
    for j in range(num):
        if lst[j+1] > avg:
            overN += 1
    print('%.3f%%' % (overN*100/num))   # 문자열 포맷 코드