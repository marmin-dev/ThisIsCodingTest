def solution(brown, yellow):
    i = 0
    while True:
        i += 1
        yel_x = yellow / i
        if yellow % i != 0:
            continue
        else:
            if 2 * (yel_x + 2) + 2 * i == brown:
                answer = [yel_x + 2, i + 2]
                break

    return answer