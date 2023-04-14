def card_game():
    result = 0
    n, m = map(int, input().split())
    for a in range(n):
        data = list(map(int,input().split()))
        min_value = 10001
        for b in data:
            min_value = min(min_value,b)
        result = max(result, min_value)
    return result
print(card_game())