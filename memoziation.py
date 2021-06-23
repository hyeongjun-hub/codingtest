# 솔희는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다. 그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...
# 가능한 최대 수익을 리턴시켜 주는 함수 max_profit_memo 를 Memoization 방식으로 작성해 보세요. max_profit_memo는 파라미터 세 개를 받습니다.
# price_list: 개수별 가격이 정리되어 있는 리스트
# count: 판매할 새꼼달꼼 개수
# cache: 개수별 최대 수익이 저장되어 있는 사전

def max_profit_memo(price_list, count, cache):
    list1 = []

    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for x in range(1, count // 2 + 1):
        list1.append(max_profit_memo(price_list, x, cache) + max_profit_memo(price_list, count - x, cache))
        list1.append(profit)
    cache[count] = max(list1)
    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
