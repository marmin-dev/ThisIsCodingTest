import time

def big():
    idx, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    start = time.time()
    data.sort()
    # data.reverse()
    count = 0
    for a in range(1, m+1):
        if a % (k + 1) == 0:
            count += data[-2]
            print(data[-2])
        else:
            count += data[-1]
            print(data[-1])
    end = time.time()
    print("time : ", end - start)
    return(count)

print(big())


