# 2020/10/04 (일)

lst = []
for i in range(10):
    num = int(input())
    lst.append(num % 42)

print(len(set(lst)))