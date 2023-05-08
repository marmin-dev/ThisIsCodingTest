def solution(id_list, report, k):
    ans = []
    answer = []
    for a in range(len(id_list)):
        ans.append(0)
        answer.append(0)
    report = set(report)
    dd =[]
    for a in report:
        dd.append(a.split(' '))
    for i in range(len(dd)):
        for j, b in enumerate(id_list):
            if dd[i][1] == b:
                ans[j] += 1
    for j, a in enumerate(ans):
        if a >= k:
            for b in dd:
                if id_list[j] == b[1]:
                    for c, d in enumerate(id_list):
                        if b[0] == d:
                            answer[c] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))