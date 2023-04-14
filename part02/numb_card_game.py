def card_game():
    n, m = map(int, input().split())
    for a in range(n):
        data = list(map(int,input().split()))
        min_num = []
        min_num.append(min(data))
    return max(min_num)
print(card_game())