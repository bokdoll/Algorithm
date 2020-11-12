# 2020/11/13 (금)
# [Chapter06-정렬 23번] 국영수

def solution():
    n = int(input()) # 학생 수
    score = []
    for i in range(n):
        score.append(list(input().split()))
    score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    answer = list(map(lambda x:x[0], score))
    return answer


if __name__ == "__main__":
    answer = solution()
    for name in answer:
        print(name)



'''
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''