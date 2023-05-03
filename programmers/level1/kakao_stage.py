def solution(N, stages):
    stages1 = []
    stages.sort()
    stages_p = []
    for a in range(1,N+2):
        stages_p.append(stages.count(a))
    print(stages_p)
    for i, a in enumerate(stages_p):
        stg_p = 0
        if i == N :
            break
        else:
            for b in stages_p[i:]:
                stg_p += b
        if a == 0:
            stages1.append((i+1 , 0))
        else:
            stages1.append((i + 1, a/stg_p))
    stages1.sort(key = lambda x:x[1])
    stages1.reverse()
    for a in range(len(stages1) -1):
        for b in range(a + 1,len(stages1)):
            if stages1[a][1] == stages1[b][1]:
                if stages1[a][0] > stages1[b][0]:
                    temp = stages1[a]
                    stages1[a] = stages1[b]
                    stages1[b] = temp
    answer = []
    for a in range(len(stages1)):
        answer.append(stages1[a][0])
    return answer


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))