# 2020/11/13 (금)
# 정렬-단어 정렬


def solution():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    words = set(words)
    return sorted(words, key=lambda x: (len(x), x))


if __name__ == "__main__":
    answer = solution()
    for item in answer:
        print(item)