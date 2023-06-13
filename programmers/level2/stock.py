def solution(prices):
    answer = []
    for i, p in enumerate(prices):
        count = 0
        for b in prices[i + 1:]:
            count += 1
            if b < p:
                break
        answer.append(count)
    return answer