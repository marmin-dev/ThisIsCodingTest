def solution(clothes):
    answer = 1
    cat = {}
    for a in clothes:
        if not a[1] in cat:
            cat[a[1]] = [a[0]]
        else:
            cat[a[1]].append(a[0])
    cat = list(cat.items())
    for a in cat:
        answer *= (len(a[1]) + 1)
    return answer - 1