# 2020/09/24 (목)

def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)

    if citations[-1] >= n:  # citaions[-1] = min
        return n

    num = dict()
    _max = citations[0]

    num[_max] = citations.count(_max)
    if num[_max] >= _max:
        return _max

    for c in range(_max-1, 0, -1):
        num[c] = num[c+1]
        if c in citations:
            num[c] += citations.count(c)
        if num[c] >= c and c <= n:
            return c


if __name__ == '__main__':
    citations = [12, 11, 10, 9, 8, 1]
    print(solution(citations))