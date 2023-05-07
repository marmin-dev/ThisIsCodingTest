# def solution(lottos, win_nums):
#     lottos.sort()
#     win_nums.sort()
#     count = 0
#     count_0 = 0
#     answer = []
#     if lottos == win_nums:
#         return [1,1]
#     elif lottos == [0,0,0,0,0,0]:
#         return [1,6]
#     for a in lottos:
#         if a == 0:
#             count_0 += 1
#             continue
#         for b in win_nums:
#             if a == b:
#                 count += 1
#     # if count_0 > 4:
#     #     if count == 1:
#     #         return [1,6]
#     #     elif count == 0:
#     #         return [2,6]
#     # elif count > 3:
#     #     if count == 2:
#     #         return [1,6]
#     #     elif count == 1:
#     #         return [2,6]
#     #     else:
#     #         return
#     counter = 6
#     for a in range(0,6):
#         counter -= 1
#         if a == count:
#             answer.append(counter)
#     for a in range(0,6):
#         if a == count_0:
#             answer.append(answer[0] + a)
#     answer.sort()
#     return answer
def solution(lottos, win_nums):
    lottos2 = []
    count = 0
    answer = []
    for a in lottos:
        if a != 0:
            lottos2.append(a)
    count_0 = len(lottos) - len(lottos2)
    for a in lottos2:
        if a in win_nums:
            count += 1
    if count > 0:
        answer.append(7 - count - count_0)
        answer.append(7 - count)
    else:
        if count_0 == 0:
            answer.append(6)
        else:
            answer.append(7 - count_0)
        answer.append(6)
    return answer


print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))