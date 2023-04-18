def solution(s):
    s = list(s)
    s.sort()
    s_s = set()
    s_l = []
    for a in s:
        if s.count(a) != 1:
            s_s.add(a)
    for b in s:
        if b in s_s:
            pass
        else:
            s_l.append(b)
    answer = ''.join(s_l)
    return answer
print(solution("abcabcadc"))