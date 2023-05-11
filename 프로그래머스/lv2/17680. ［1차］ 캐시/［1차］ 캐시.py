def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        # print(city)
        city = city.lower()
        if not city in cache: # 없는 도시일 때, 캐시 사이즈보다 작으면 넣고, 크면 마지막 원소를 뺀 다음 앞에다 넣어야하네 맨 앞에
            if len(cache) < cacheSize:
                cache.insert(0, city)
                # print(cache)
            else:
                cache.insert(0, city)
                cache.pop()
                # print(cache)
            answer += 5
        else: # 만약 있는 도시면 그 도시를 뽑아서 맨 앞에다 넣고 길이 확인 후 마지막 원소 지워버리기
            city_idx = cache.index(city)
            cache.remove(cache[city_idx])
            cache.insert(0, city)
            if len(cache) > cacheSize:
                cache.pop()
            # print(cache)
            answer += 1
    return answer