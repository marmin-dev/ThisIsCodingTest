def solution(d, budget):
    d.sort()
    dd = 0
    answer = 0
    for a in d:
        dd += a
        if budget >= dd:
            answer += 1
        else:
            break
    return answer


print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))