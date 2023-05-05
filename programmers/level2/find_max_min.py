def solution(s):
    li_num = s.split(' ')
    li_int = []
    for a in li_num:
        li_int.append(int(a))
    a = max(li_int)
    b = min(li_int)
    answer = f'{b} {a}'
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))