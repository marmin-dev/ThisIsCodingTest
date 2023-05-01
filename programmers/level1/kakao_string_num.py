def solution(s):
    str_li = ['zero','one','two','three','four','five','six','seven','eight','nine']
    b=''
    str_ans = []
    for a in s:
        if a.isdigit():
            str_ans.append(a)
            continue
        b += a
        for i, c in enumerate(str_li):
            if b == c:
                str_ans.append(str(i))
                b = ''
    answer = int(''.join(str_ans))
    return answer

print(solution("one4seveneight"))