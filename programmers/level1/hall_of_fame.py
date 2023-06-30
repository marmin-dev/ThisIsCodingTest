def solution(k, score):
    answer = []
    fame = []
    for a in score:
        fame.append(a)
        fame.sort(reverse=True)
        if len(fame) > k:
            fame.pop()
        answer.append(fame[-1])
    return answer