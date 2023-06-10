# 정확성 100 효율성 50
# def solution(phone_book):
#     if len(phone_book) == 1:
#         return True
#     answer = True
#     phone_book.sort(key = lambda k : len(k), reverse=True)
#     for i in range(len(phone_book)):
#         aa = phone_book.pop()
#         for a in phone_book:
#             if aa == a[:len(aa)]:
#                 answer = False
#                 return answer
#     # print(phone_book)
#     return answer

def solution(phone_book):
    answer = True
    if len(phone_book) == 1:
        return True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return answer