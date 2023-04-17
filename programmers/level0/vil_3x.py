def solution(n):
    b =[]
    for a in range(1,300):
        if "3" in str(a) or a % 3 ==0:
            pass
        else:
            b.append(a)
    answer = b[n - 1]
    return answer

print(solution(15))