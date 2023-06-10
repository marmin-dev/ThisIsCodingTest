# def solution(n, left, right):
#     answer = []
#     d_ans = []
#     for i in range(n):
#         d_ans.append([])
#         for b in range(n):
#             if b + 1 <= i + 1:
#                 d_ans[i].append(i + 1)
#             else:
#                 d_ans[i].append(b + 1)
#     for a in d_ans:
#         answer.extend(a)
#     return answer[left:right+1]
# 답은 맞지만 런타임에러
# 정답 코드
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        answer.append(max(a+1,b+1))
    return answer