def solution(numbers):
    answer = set()
    for a in range(len(numbers) - 1):
        for b in range(a + 1,len(numbers)):
            answer.add(numbers[a] + numbers[b])
    answer = list(answer)
    return answer

print(solution([2,1,3,4,1]))