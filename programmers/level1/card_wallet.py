def solution(sizes):
    answer = 0
    for i, x in enumerate(sizes):
        sizes[i].sort()
    sizes.sort(key=lambda x:x[0])
    size1 = sizes[-1][0]
    sizes.sort(key=lambda x:x[1])
    size2 = sizes[-1][1]
    answer = size1 * size2
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))