def solution(numbers, hand):
    key_dict = {1:(1,1),2:(2,1),3:(3,1),4:(1,2),5:(2,2),6:(3,2),7:(1,3),8:(2,3),9:(3,3),0:(2,4)}
    l_hand = (1,4)
    r_hand = (3,4)
    answer = []
    for a in numbers:
        x, y = key_dict[a]
        if x == 1:
            answer.append('L')
            l_hand = key_dict[a]
        elif x == 3:
            answer.append('R')
            r_hand = key_dict[a]
        elif x == 2:
            xl, yl = l_hand
            xr, yr = r_hand
            l_h = abs(xl - x) + abs(yl - y)
            r_h = abs(xr - x) + abs(yr - y)
            if l_h > r_h:
                answer.append('R')
                r_hand = key_dict[a]
            elif r_h > l_h:
                answer.append('L')
                l_hand = key_dict[a]
            elif r_h == l_h:
                if hand == 'right':
                    answer.append('R')
                    r_hand = key_dict[a]
                else:
                    answer.append('L')
                    l_hand = key_dict[a]
    answer = ''.join(answer)
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'))