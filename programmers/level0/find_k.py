def solution(i, j, k):
    k = str(k)
    answer = 0
    for a in range(j - i + 1):
        for s in str(i + j):
            if s == k:
                answer += 1
    return answer