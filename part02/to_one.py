def to_one():
    n, k = map(int,input().split())
    count = 0
    while n != 1:
        if n % k != 0:
            n -= 1
            count += 1
        else:
            n = n/k
            count += 1
    return count
print(to_one())