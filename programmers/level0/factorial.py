def solution(n):
    max = 3628800
    answer = 0
    ax = 1
    print(n)
    for a in range(0,10):
        if n >= max / ax:
            answer = 10 - a
            break
        ax *= (10 - a)
    return answer

print(solution(24))