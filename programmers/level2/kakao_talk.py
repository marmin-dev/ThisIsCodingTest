def solution(record):
    arr = []
    arr_id = {}
    answer = []
    for rec in record:
        arr.append(rec.split(' '))
    for a in arr:
        print(a)
        if a[0] == "Enter":
            arr_id[a[1]] = a[2]
        elif a[0] == "Change":
            arr_id[a[1]] = a[2]
    for a in arr:
        if a[0] == "Enter":
            answer.append(f'{arr_id[a[1]]}님이 들어왔습니다.')
        elif a[0] == "Leave":
            answer.append(f'{arr_id[a[1]]}님이 나갔습니다.')
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

