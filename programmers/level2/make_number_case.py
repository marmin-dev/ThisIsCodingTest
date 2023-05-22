# 정확성만 맞음 효율성은 떨어짐
# def solution(n):
#     answer = 0
#     for a in range(1, n + 1):
#         temp = 0
#         for b in range(a , n + 1):
#             temp += b
#             if temp == n:
#                 answer += 1
#                 continue
#             elif temp > n:
#                 continue
#     return answer
# Dynamic Programming 으로 풀기
# def solution(n):
#     dp = [0] * (n + 1)  # DP 테이블 초기화
#     dp[0] = 1
#
#     for i in range(1, n + 1):
#         for j in range(i, n + 1):
#             if n == dp[j] + dp[j - i]:
#                 dp[j] += dp[j - i]
#     return dp[n]
#
# 브루트 포스 방식
def solution(n):
    answer = 0
    start = 1
    end = 1
    total = 0

    while start <= n:
        if total < n:
            total += end
            end += 1
        elif total > n:
            total -= start
            start += 1
        else:
            answer += 1
            total -= start
            start += 1

    return answer
print(solution(15))