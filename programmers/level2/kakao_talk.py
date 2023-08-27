def solution(record):
    arr = []
    arr_id = {}
    for rec in record:
        arr.append(rec.split(' '))
    for a in arr:
        print(a)
        if arr[0] == "Enter":
            arr_id[a[1]] = a[2]
        elif arr[0] == "Change":
            arr_id[a[1]] = a[2]
    print(arr_id)

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

