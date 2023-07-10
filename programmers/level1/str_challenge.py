def solution(s):
    answer = 0
    count_x = 0
    count_y = 0
    x = ''
    for i, a in enumerate(s):
        if x == '':
            x = a
        if x == a:
            count_x += 1
            print('x:', count_x)
        else:
            count_y += 1
            print('y:', count_y)
        if count_x != 0 and count_x == count_y:
            answer += 1
            count_x = 0
            count_y = 0
            x = ''
            print(a)
        elif i == len(s) - 1:
            answer += 1

    return answer