def solution(answers):
    answer = []
    # 사람의 정답 맞춘수
    fir = 0
    sec = 0
    thi = 0
    # 2번
    second = '21232425'
    # 3번
    third = '3311224455'
    for i in range(len(answers)):
        if (i % 5) + 1 == answers[i]:
            fir += 1
        if int(second[i % len(second)]) == answers[i]:
            sec += 1
        if int(third[i % len(third)]) == answers[i]:
            thi += 1
    a = max([fir,sec,thi])
    for i,b in enumerate([fir,sec,thi]):
        if b == a:
            answer.append(i + 1)
    return answer