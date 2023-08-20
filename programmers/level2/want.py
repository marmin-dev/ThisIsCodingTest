def solution(want, number, discount):
    answer = 0
    for a in range(len(discount)):
        init_number = number.copy()
        if len(discount) >= a + 10:
            for b in range(0,10):
                for i,c in enumerate(want):
                    if c == discount[a + b]:
                        init_number[i] -= 1
                if init_number.count(0) == len(number):
                    answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],
         [3, 2, 2, 2, 1],
         ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))