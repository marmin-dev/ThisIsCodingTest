def solution(s):
    answer = 0
    li = []
    s = list(s)
    aa = True
    while aa:
        sa = s.pop()
        if not s:
            answer = 0
            break
        if sa == s[-1]:
            s.pop()
            s.extend(li)
            li = []
        else:
            li.append(sa)
        if not s and not li:
            answer = 1
            aa = False
    return answer

# print(solution('baabaa'))
print(solution('cdcd'))