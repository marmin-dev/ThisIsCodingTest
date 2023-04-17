import math
def solution(my_str, n):
    answer = []
    a = 0
    print(len(my_str))
    for m in range(1,math.ceil(len(my_str)/n)+1):
        if a <= len(my_str):
            print(m)
            answer.append(my_str[a:m * n])
            a += n
            print(a)
        else:
            print(a)
            answer.append(my_str[a:])
    return answer
print(solution("abc1Addfggg4556b",6))