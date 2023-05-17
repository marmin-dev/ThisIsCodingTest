def solution(s, n):
    answer = ''
    for a in s:

        if a == ' ':
            answer += a
        else:
            if ord(a) + n > 90 and ord(a) <= 90:
                answer += chr(65 + n - 1)
            elif ord(a) + n < 65 and ord(a) >= 65:
                answer += chr(90 + n + 1)
            elif ord(a) + n > 122 and ord(a) <= 122:
                answer += chr(97 + n - 1)
            elif ord(a) + n < 97 and ord(a) >= 97:
                answer += chr(122 + n + 1)
            else:
                answer += chr(ord(a) + n)
    return answer
# answer code
# def solution(s, n):
#     answer = ''
#     for c in s:
#         for i in range(n):
#             if c not in (' ', 'z', 'Z'):
#                 c = chr(ord(c)+1)
#             elif c in ('z', 'Z'):
#                 c = chr(ord(c)-26 + 1)
#             else:
#                 break
#         answer += c
#     return answer
print(solution("AB",1))