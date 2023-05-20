def solution(m,li):
    li.sort()
    for h in range(max(li),1,-1):
        li2 = []
        for a in li:
            if a - h > 0:
                li2.append(a - h)
            else:
                pass
        if sum(li2) == m:
            return h

print(solution(6, [19,15,10,17]))


