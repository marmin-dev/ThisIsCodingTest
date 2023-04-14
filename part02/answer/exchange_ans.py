import time
def exchange(n):
    start = time.time()
    count =0
    # 큰 단위의 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += n // coin
        n %= coin
    end = time.time()
    print("time : ", end - start)
    return count

print(exchange(1260))