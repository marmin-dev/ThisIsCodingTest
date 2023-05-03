def solution(a, b):
    mon_li = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_li = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days = 0
    for a in range(a-1):
        days += mon_li[a]
    days += b
    l_day = days % 7
    answer = day_li[l_day - 1]
    return answer

print(solution(5,24))