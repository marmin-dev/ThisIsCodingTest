def solution(a,b):
    answer = 0
    a.sort()
    b.sort(reverse=True)
    for i , n in enumerate(a):
        answer += n * b[i]
    return answer