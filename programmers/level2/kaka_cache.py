# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return 5 * len(cities)
#     for idx, city in enumerate(cities):
#         cities[idx] = city.lower()
#         if ' ' in city:
#             cities[idx] = city.replace(' ','')
#     cache = []
#     for a in range(cacheSize):
#         cache.append('0')
#     answer = 0
#     for city in cities:
#         count = 0
#         ca_list = []
#         for idx, ca in enumerate(cache):
#             # hit
#             if ca == city:
#                 ca_list = cache.copy()
#                 temp = ca_list[-1]
#                 ca_list[-1] = city
#                 ca_list[idx] = temp
#                 count += 1
#                 continue
#             else:
#                 pass
#         if count == 0:
#             cache.pop(0)
#             cache.append(city)
#             answer += 5
#         else:
#             cache = ca_list.copy()
#             answer += 1
#     return answer
#
# print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5 * len(cities)
    # 캐시 크기의 데크 선언
    cache = deque(maxlen=cacheSize)
    for a in cities:
        if len(cache) == cacheSize:
            if not a.lower() in cache:
                cache.popleft()
                cache.append(a.lower())
                answer += 5
            else:
                cache.remove(a.lower())
                cache.append(a.lower())
                answer += 1
        else:
            if not a.lower() in cache:
                cache.append(a.lower())
                answer += 5
            else:
                cache.remove(a.lower())
                cache.append(a.lower())
                answer += 1
    return answer