def solution(id_list, report, k):
    answer = []
    report_set = set()
    id_li = []
    for a in range(len(id_list)):
        answer.append(0)
    for a in id_list:
        id_li.append([a,0])
    for a in report:
        b = a.split(' ')
        b = tuple(b)
        report_set.add(b)
    for a,b in report_set:
        for c in id_li:
            if b == c[0]:
                c[1] += 1
    for i, a in enumerate(id_li):
        if a[1] >= k:
            for l, b in report_set:
                if a[0] == b:
                    for j, c in enumerate(id_list):
                        if l == c:
                            answer[j] +=1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))