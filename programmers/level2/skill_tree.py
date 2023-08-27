def solution(skill, skill_trees):
    # 가능한 조건 개수 세는 변수
    count = 0
    # 1차 반복문 시작
    for s in range(len(skill_trees)):
        # 인덱스 값
        idx = 0
        # 2차 반복문 시작
        for k in range(len(skill_trees[s])):
            if skill_trees[s][k] == skill[idx]:
                idx += 1

    return count