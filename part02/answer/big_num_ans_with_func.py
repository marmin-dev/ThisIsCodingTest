import time

def big():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    start = time.time()
    data.sort() # 입력받은 수들 정렬하기

    first = data[n - 1] # 가장 큰 수
    second = data[n - 2] # 두 번째로 큰 수

    # 가장 큰 수가 더해지는 연산
    count = int(m / (k+1) * k)
    count += m % (k + 1)

    result = 0
    result += (count) * first
    result += (m - count) * second


    end = time.time()
    print("time : ", end - start)
    return result

print(big())