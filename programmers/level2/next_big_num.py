def solution(n):
    answer = n
    flag = True
    binar = bin(n).split('b')[1].count('1')
    print(binar)
    while flag:
        answer += 1
        binar2 = bin(answer).split('b')[1].count('1')
        if binar2 == binar:
            flag = False
    return answer