def solution(arr):
    answer = []
    for a in range(len(arr)):
        b = arr.pop()
        if a == 0:
            answer.append(b)
            continue
        if b == answer[-1]:
            pass
        else:
            answer.append(b)
    answer.reverse()
    return answer

print(solution([1,1,3,3,0,1,1]))