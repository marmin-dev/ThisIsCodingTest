def solution(priorities, location):
    answer = 0
    # 튜플로 원소의 이름 짓기
    pri = []
    process = []
    for i,a in enumerate(priorities):
        pri.append((i,a))
    # pri가 0 이 될때까지 실행 순서를 process에 추가
    while len(pri) != 0:
        a = pri.pop(0)
        if a[1] >= max(priorities):
            priorities.remove(max(priorities))
            process.append(a)
        else:
            pri.append(a)
    for i, a in enumerate(process):
        if location == a[0]:
            answer = i + 1
    return answer