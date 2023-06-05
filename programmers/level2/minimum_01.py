def solution(name):
    answer = 0
    n_ord = []
    for a in name:
        if ord(a) < 79:
            answer += ord(a) - 65
        else:
            answer += abs(90 - ord(a)) + 1
    if name[1] == "A":
        for i,a in enumerate(name):
            if a != 'A' and i > 1:
                n = i
        answer += len(name) - (len(name[:n]))
    else:
        answer += len(name) - 1
    return answer