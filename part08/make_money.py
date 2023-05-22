def solution(n, m):
    d = [10001] * (m + 1)
    d[0] = 0
    for i in range(len(n)):
        # print(i)
        for j in range(n[i], m + 1):
            if d[j - n[i]] != 10001:
                # print(j)
                d[j] = min(d[j], d[j - n[i]] + 1)
    if d[m] == 10001:
        return -1
    else:
        return d[m]

print(solution([2,3],15))