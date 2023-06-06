def solution(park, routes):
    answer = []
    for i,a in enumerate(park):
        for k,b in enumerate(a):
            if b == 'S':
                answer = [i,k] # 시작점 찾기
    # 이동 경로
    for a in routes:
        if a[0] == 'E':
            answer[1] += int(a[2])
        elif a[0] == 'W':
            answer[1] -= int(a[2])
        elif a[0] == 'S':
            answer[0] += int(a[2])
        else:
            answer[0] -= int(a[2])
    return answer