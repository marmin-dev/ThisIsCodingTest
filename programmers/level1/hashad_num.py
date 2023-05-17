def solution(x):
    x1 = str(x)
    x2 = 0
    for a in x1:
        x2 += int(a)
    if x % x2 == 0:
        answer = True
    else:
        answer = False
    return answer