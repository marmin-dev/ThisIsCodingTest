def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    for idx, city in enumerate(cities):
        cities[idx] = city.lower()
        if ' ' in city:
            cities[idx] = city.replace(' ','')
    cache = []
    for city in cities:
        count = 0
        ca_list = []
        for idx, ca in enumerate(cache):
            # hit
            if ca == city:
                ca_list = cache.copy()
                temp = ca_list[-1]
                ca_list[-1] = city
                ca_list[idx] = temp
                count += 1
                continue
            else:
                pass
        if count == 0:
            cache.pop(0)
            cache.append(city)
            answer += 5
        else:
            cache = ca_list.copy()
            answer += 1
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))