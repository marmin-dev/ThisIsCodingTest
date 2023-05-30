def solution(t, p):
    answer = 0
    for a in range(0, len(t) - len(p) + 1):
        if int(t[a:a + len(p)]) <= int(p):
            answer += 1
    return answer