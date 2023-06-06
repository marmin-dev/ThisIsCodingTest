def solution(s):
    answer = []
    for i, a in enumerate(s):
        if i == 0:
            answer.append(-1)
            continue
        b = s[:i].rfind(a)
        if b == -1:
            answer.append(b)
        else:
            answer.append(i-b)
    return answer