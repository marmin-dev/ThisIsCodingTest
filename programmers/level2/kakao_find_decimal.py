# 정답률 60%
# def solution(n, k):
#     answer = 0
#     div = ""
#     div2 = []
#     while n > 0:
#         div = str(n % k) + div
#         n //= k
#     div = div.split('0')
#     for a in div:
#         if a == '2':
#             answer += 1
#         elif a == '':
#             pass
#         elif a == '1':
#             pass
#         else:
#             div2.append(int(a))
#     for a in div2:
#         c = 0
#         for b in range(3, a, 2):
#             if a % 2 == 0:
#                 c += 1
#                 break
#             else:
#                 pass
#         if c == 0:
#             answer += 1
#
#     return answer