def solution(array):
    answer = 0
    for n in array:
        answer += str(n).count('7')
    return answer

print(solution([7, 77, 17]))