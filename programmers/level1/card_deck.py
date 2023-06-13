# 88 %
# def solution(cards1, cards2, goal):
#     answer = 'No'
#     while goal:
#         a = goal.pop()
#         if cards1:
#             if a == cards1[-1]:
#                 cards1.pop()
#         if cards2:
#             if a == cards2[-1]:
#                 cards2.pop()
#     if cards1 or cards2:
#         pass
#     else:
#         answer = 'Yes'
#     return answer
def solution(cards1, cards2, goal):
    for target in goal:
        if len(cards1) and target == cards1[0]: cards1.pop(0)
        elif len(cards2) and target == cards2[0]: cards2.pop(0)
        else: return 'No'
    return 'Yes'