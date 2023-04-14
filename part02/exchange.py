import time

def change(money):
    start = time.time()
    m1 = money % 500
    coin = 0
    coin += (money//500)
    money = (m1 % 100)
    coin += (m1 // 100)
    m1 = (money % 50)
    coin += (money // 50)
    coin += m1 // 10
    end = time.time()
    print("time : ",end - start)
    return coin

print(change(1260))