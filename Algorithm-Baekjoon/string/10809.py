# 2020/10/08 (목)

word = input()
answer = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for a in alphabet:
    if a in word:
        answer += str(word.index(a))
    else:
        answer += '-1'
    answer += ' '
print(answer)