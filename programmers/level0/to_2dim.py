def solution(num_list, n):
    answer = []
    for a in range(int(len(num_list)/n)):
        answer.append(num_list[n * a: n * a + n])
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8],2))