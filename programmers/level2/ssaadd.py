def solution(s):
    stack = []
    if len(s) % 2 != 0:
        return 0
    i = 0
    while i < len(s):
        if not stack:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    if stack:
        return 0
    else:
        return 1

# use stack