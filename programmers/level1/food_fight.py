def solution(food):
    ans = ''
    for i,a in enumerate(food):
        ans += str(i) * (a//2)
    answer = ans + '0'
    ans = list(ans)
    ans.reverse()
    ans = ''.join(ans)
    answer += ans
    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))