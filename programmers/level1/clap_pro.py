def solution(n):
    answer = ''
    for a in range(n):

        if a % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

print(solution(3))