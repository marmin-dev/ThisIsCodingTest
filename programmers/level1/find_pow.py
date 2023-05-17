def solution(n):
    if not(n ** 0.5).is_integer():
        answer = -1
    else:
        answer = ((n ** 0.5) + 1) ** 2
    return int(answer)



print(solution(121))
print(solution(12))