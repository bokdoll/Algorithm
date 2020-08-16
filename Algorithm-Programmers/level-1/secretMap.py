# 2020/08/10 (월)
def solution(n, arr1, arr2):
    bin_arr1 = binarize(arr1, n)
    bin_arr2 = binarize(arr2, n)

    arr = []
    for i in range(n):
        # 2. arr1 + arr2 0이 아니면 다 1
        merged_array = list(map(lambda x, y: '0' if int(x) + int(y) == 0 else '1', bin_arr1[i], bin_arr2[i]))
        str_num = ''.join(merged_array)
        # 3. 1은 # 0은 ' '으로 change
        arr.append(str_num.replace('1', '#').replace('0', ' '))
    return arr


def binarize(array, n):
    # 1. arr1, arr2를 각각 이진수로 변환
    # python 내장함수 : bin(x), oct(x), hex(x)
    bin_arr = list(map(lambda x: bin(x)[2:], array))

    # 2-1. 자리수(n) 맞추기
    # 길이가 n이면 그대로, 그렇지 않으면 len(x)-n만큼의 0을 앞에 붙이기
    return list(map(lambda x: x if len(x) == n else '0' * (n - len(x)) + x, bin_arr))

if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
