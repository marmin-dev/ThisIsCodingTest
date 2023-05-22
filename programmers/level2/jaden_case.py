def solution(s):
    s = s.lower()
    answer = ''
    s = s.split(' ')
    for a in s:
        if a.isalpha():
            if a == s[0]:
                answer = a.capitalize()
                continue
            answer += ' ' + a.capitalize()
        else:
            if a == s[0]:
                answer = a
                continue
            answer +=' ' + a
    return answer