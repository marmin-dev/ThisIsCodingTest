# 시간 복잡도는 맞지만 정확성 오류
# def solution(s):
#     s = list(s)
#     if s[0] == ')' or s[-1] == '(':
#         return False
#     if s.count('(') == s.count(')'):
#         return True
#     else:
#         return False

# pop 사용
def solution(s):
    s = list(s)
    count1 = 0
    count2 = 0
    if s[-1] == '(' or s[0] == ')':
        return False
    for i in range(len(s)):
        sa = s.pop()
        if sa == ')':
            count1 += 1
        else:
            count2 += 1
        if count1 < count2:
            return False
    if count1 == count2:
        return True