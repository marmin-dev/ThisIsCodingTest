def solution(arr):
    d = [0] * 10000
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        d[i] = max(d[i - 1], d[i - 2] + arr[i])
        print(d[i])
    return d[len(arr) - 1]
print(solution([1,3,1,5,9,1,5]))