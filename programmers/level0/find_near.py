def solution(array, n):
    answer = array[0]
    for a in array:
        if n - a < 0:
            if a - n < abs(n - answer):
                answer = a
        elif n -a > 0:
            if n - a < abs(n-answer):
                answer = a
        else:
            answer = a
    return answer