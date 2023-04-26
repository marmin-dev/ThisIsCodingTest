def solution(n):
    an = []
    answer = 0
    while n // 3 != 0:
        n1 = n % 3
        n = n // 3
        an.append(n1)
    an.append(n % 3)
    an.reverse()
    for a in range(len(an)):
        answer += pow(3,a) * an[a]
    return answer




print(solution(45))