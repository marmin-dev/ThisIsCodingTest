import copy


def solution(land):
    answer = 0
    arr = []

    # print(max([1, 2, 3, 4]))
    for a in range(4):
        idx = a
        answer = 0
        answer += land[0][a]
        lander = copy.deepcopy(land)
        for l in range(1, len(land)):
            lander[l].pop(idx)
            answer += max(lander[l])
            idx = lander[l].index(max(lander[l]))
        arr.append(answer)
        print(arr)
        answer = max(arr)


    return answer
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))