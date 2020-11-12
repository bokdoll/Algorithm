# 2020/11/12 (목)
# [Chapter06-정렬 실전문제] 두 배열의 원소 교체

def solution():
    N, K = map(int, input().split())    # N: 원소의 개수, K: 바꿔치기 개수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)

    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
    return sum(A)

if __name__ == "__main__":
    print(solution())