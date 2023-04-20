def solution(polynomial):
    polynomial = polynomial.split(' + ')
    x_li = []
    num = []
    li2=0
    li3=0
    answer = polynomial
    for a in polynomial:
        if 'x' in a:
            x_li.append(a)
        else:
            num.append(a)
    for b in num:
        li2 += int(b)
    for c in x_li:
        d = c.replace('x','')
        print(d)
        li3 += int(d)
    # answer = f"{li3}x + {li2}"

print(solution("3x + 7 + x"))