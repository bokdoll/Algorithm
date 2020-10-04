# 2020/10/04 (일)

n = int(input())
lst = list(map(float, input().split()))
_max = max(lst)
sum = 0
for i in range(n):
    lst[i] = (lst[i] / _max) * 100
    sum += lst[i]
print(sum / n)
