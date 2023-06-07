def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for a in citations:
        if a > answer:
            answer += 1

    return answer