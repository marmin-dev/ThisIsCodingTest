

def solution(emergency):
    temp = emergency.copy()
    emergency.sort()
    answer = []
    for a in temp:
        for i, b in enumerate(emergency):
            if a == b:
                answer.append(i+1)
    return answer

print(solution([7, 6, 5, 4, 3, 2, 1]))