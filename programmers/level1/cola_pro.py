def solution(a, b, n):
    answer = 0
    while n // a != 0:
        cola = 0
        # 받는 콜라의 개수
        cola = n // a
        # 남는 빈병의 개수
        n = n % a + cola
        answer += cola
    return answer
