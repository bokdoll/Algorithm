# 2020/11/20 (금)

def solution(n, times):
    start, end = 1, n * min(times)
    while start < end:
        mid = (start + end) // 2
        total = sum([mid // t for t in times])
        if total < n:
            start += 1
        elif total >= n:
            end = mid
    return start


if __name__ == "__main__":
    print(solution(n=22, times=[5, 7, 10, 11, 15, 23]))
