def solution(ingredient):
    answer = 0
    stack = []
    for a in ingredient:
        stack.append(a)
        if len(stack) >= 4:
            # print(stack)
            if stack[-4:] == [1, 2, 3, 1]:
                for a in range(4):
                    stack.pop()
                answer += 1
    return answer
