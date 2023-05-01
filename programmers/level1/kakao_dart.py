def solution(dartResult):
    shot_li = []
    shot = ''
    # make string to list
    for i,a in enumerate(dartResult):
        if i > 0 and a.isdigit():
            shot_li.append(shot)
            shot = ''
        elif i == len(dartResult) - 1:
            shot += a
            shot_li.append(shot)
            continue
        shot += a
    shoot = []
    # if 10 exists in the shot
    for i,a in enumerate(shot_li):
        if i != 0:
            if shot_li[ i -1 ] == "1":
                continue
        if a == '1':
            shoot.append(shot_li[i] + shot_li[i + 1])
        else:
            shoot.append(a)
    # dart logic
    answer = [0,0,0]
    for i,a in enumerate(shoot):
        for j,b in enumerate(a):
            if b == '0':
                continue
            elif b == '1' and a[j + 1] == '0':
                answer[i] = 10
            elif b.isdigit():
                answer[i] = int(b)
            elif b in ['S','D','T']:
                for k ,c in enumerate(['S','D','T']):
                    if b == c:
                        answer[i] **= k+1
            elif b in ['#','*']:
                if b =='#':
                    answer[i] *= -1
                else:
                    if answer[i - 1]:
                        answer[i -1] *= 2
                        answer[i] *=2
                    else:
                        answer[i] *= 2
    ans = sum(answer)
    return ans



