def solution(s):
    answer = ''
    ans = []
    ee = ''
    for i,a in enumerate(s):
        if a == s[-1]:
            ee += a
            ans.append(ee)
        elif a.isalpha() and s[i+1].isalpha():
            ee += a
        elif a.isalpha() and s[+1] == ' ':
            ee += a
            ans.append(ee)
            ee = ''
        elif a == ' ' and s[i+1] == ' ':
            ee += a
        else:
            ee += a
            ans.append(ee)
            ee = ''
    for a in ans:
        dd = ''
        if a[0] == ' ':
            answer += a
        else:
            for i,x in enumerate(a):
                if i % 2 == 0:
                    dd += x.upper()
                else:
                    dd += x.lower()
        answer += dd
    return answer

print(solution("try  hello world"))
