def solution(n):
    answer = 1
    for a in range(1, n +1,2):
        count = 0
        if a == 1:
            continue
        else:
            for b in range(1,a+1):
                if a % b == 0:
                    count += 1

                else:
                    continue
                if count >= 3:
                    break
            if count == 2:
                answer += 1
                print(a)

    return answer

print(solution(10))