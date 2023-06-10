# from collections import deque
#
# def solution(progresses, speeds):
#     answer = []
#     progresses = deque(progresses)
#     speeds = deque(speeds)
#     while progresses:
#         count = 0
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]
#         for a in range(len(progresses)):
#             if a >= 100:
#                 count += 1
#                 progresses.popleft()
#                 speeds.popleft()
#             else:
#                 break
#         if count != 0:
#             answer.append(count)
#     return answer
#
# print(solution([93, 30, 55], [1, 30, 5]))

def solution(progresses, speeds):
    answer = []
#    progresses = deque(progresses)
 #   speeds = deque(speeds)
    while len(progresses) != 0:
        counter = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            print(progresses[i])
        for b in progresses:
            if b >= 100:
                counter += 1
            else:
                break
        print(counter)
        if counter != 0:
            answer.append(counter)
            for i in range(counter):
                progresses.pop(0)
                speeds.pop(0)
    return answer