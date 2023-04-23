def solution(a, move):
    first = [1, 1]
    for m in move:
        if m == "L":
            if first[1] != 1:
                first[1] -= 1
        elif m == "R":
            
            if first[1] != a:
                first[1] += 1
        elif m == "U":
            if first[0] != 1:
                first[0] -= 1
        else:
            if first[0] != a:
                first[0] += 1
    return first

print(solution(5, ["R","R","R","U","D","D"]))