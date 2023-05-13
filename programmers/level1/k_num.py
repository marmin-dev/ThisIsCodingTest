def solution(array, commands):
    answer = []
    for a in commands:
        ans = array[a[0] -1 :a[1]]
        ans.sort()
        answer.append(ans[a[2] - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))