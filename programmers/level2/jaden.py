def solution(s):
    s = s.lower()
    s1 = s.split(' ')
    ans = []
    for a in s1:
        if a[0].isalpha():
            a1 = a.capitalize()
            ans.append(a1)
        else:
            ans.append(a)

    answer = ' '.join(ans)

    return answer

print(solution("3people unFollowed me"))