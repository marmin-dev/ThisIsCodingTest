def solution(new_id):
    fi_list = []
    sec_list = []
    # 1
    for n in new_id:
        if n.isalpha():
            if n.isupper():
                n = n.lower()
        fi_list.append(n)
    #print(fi_list)
    # 2
    for i, a in enumerate(fi_list):
        if a.isalpha() or a in ['-','-','.']:
            sec_list.append(a)
    #print(sec_list)
    # 3
    sec = ''.join(sec_list)
    while '..' in sec:
        sec = sec.replace('..','.')
    # 4
    if sec[0] == '.':
        sec = sec[1:]
    elif sec[-1] == '.':
        sec = sec[:len(sec)-1]
    # 5
    if sec == '':
        sec = 'a'
    # 6
    if len(sec) >= 16:
        sec = sec[:15]
    # 7
    if len(sec) <= 2:
        sec += sec + sec[-1]
    answer = sec
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))