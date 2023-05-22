def solution(s):
    answer = 0
    li = []
    s = list(s)
    while s:
        sa = s.pop()
        if sa == s[-1]:
            s.pop()
            s = s.extend(li)
            li = []
        else:
            li.append(sa)

    return answer

print(solution('baabaa'))