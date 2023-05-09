def solution(number, limit, power):
    answer = 0
    for a in range(1,number + 1):
        count = 0
        for b in range(1,a + 1):
            if a % b == 0:
                count += 1
            if count > limit:
                count = power
                break
        #print(count)
        answer += count
    return answer

print(solution(5,3,2))

print(solution(10,3,2))