def card_game():
    result = 0
    n, m = map(int, input().split())
    for a in range(n):
        data = list(map(int,input().split()))
        min_value = min(data)
        result = max(result, min_value)
    return result
print(card_game())