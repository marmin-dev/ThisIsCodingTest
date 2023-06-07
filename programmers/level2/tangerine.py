# 런타임 에러 코드

# def solution(k, tangerine):
#     answer = 0
#     counter = 0
#     tangerine.sort()
#     tan_dict = {}
#     tan_set = set(tangerine)
#     for i in tan_set:
#         tan_dict[i] = tangerine.count(i)
#     # print(tan_dict)
#     tan_dict = sorted(tan_dict.items(), key=lambda k: k[1] ,reverse= True)
#     # print(tan_dict)
#     for i in tan_dict:
#         counter += i[1]
#         answer += 1
#         if counter >= k:
#             break
#     return answer
def solution(k, tangerine):
    answer = 0
    counter = 0
    tangerine.sort()
    tan_dict = {}
    for i in tangerine:
        if not i in tan_dict.keys():
            tan_dict[i] = 1
        else:
            tan_dict[i] += 1
    tan_dict = sorted(tan_dict.items(), key= lambda k : k[1])
    while counter < k:
        counter += tan_dict.pop()[1]
        answer += 1
    return answer