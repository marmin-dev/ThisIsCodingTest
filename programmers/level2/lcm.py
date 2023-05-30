import math

def solution(arr):
    stack = []
    for lc in arr:
        if not stack:
            stack.append(lc)
        else:
            aa = stack.pop()
            stack.append(int((lc * aa) / (math.gcd(lc,aa))))
    return stack[-1]