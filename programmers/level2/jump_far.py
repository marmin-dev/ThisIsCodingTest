def solution(n):
    ds = [0] * (n + 1)
    ds[0] = 1
    ds[1] = 1
    answer = 0
    if n == 1:
        return 1
    for a in range(2, n + 1):
        ds[a] = ds[a - 1] + ds[a - 2]
    return ds[n] % 1234567