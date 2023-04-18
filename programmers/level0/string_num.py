import re

def solution(my_string):
    answer = 0
    num = re.findall(r'\d+',my_string)
    for a in num:
        answer += int(a)
    return answer

print(solution("aAb1B2cC34oOp"))